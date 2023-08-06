# pyinfra
# File: pyinfra/api/operation.py
# Desc: wraps deploy script operations and puts commands -> pyinfra._ops

'''
Operations are the core of pyinfra. The ``@operation`` wrapper intercepts calls
to the function and instead diff against the remote server, outputting commands
to the deploy state. This is then run later by pyinfra's ``__main__`` or the
:doc:`./api_operations` module.
'''

from __future__ import unicode_literals

from functools import wraps
from inspect import stack
from os import path
from types import FunctionType

import six

from pyinfra import logger, pseudo_host, pseudo_state
from pyinfra.pseudo_modules import PseudoModule

from .attrs import wrap_attr_data
from .exceptions import PyinfraError
from .host import Host
from .state import State
from .util import ensure_hosts_list, get_arg_value, make_hash, unroll_generators


class OperationMeta(object):
    def __init__(self, hash=None, commands=None):
        self.hash = hash
        self.commands = commands or []

        # Changed flag = did we do anything?
        self.changed = wrap_attr_data('changed', len(self.commands) > 0)


def add_op(state, op_func, *args, **kwargs):
    '''
    Prepare & add an operation to pyinfra.state by executing it on all hosts.

    Args:
        state (``pyinfra.api.State`` obj): the deploy state to add the operation to
        op_func (function): the operation function from one of the modules, ie \
            ``server.user``
        args/kwargs: passed to the operation function
    '''

    for host in state.inventory:
        op_func(state, host, *args, **kwargs)


def add_limited_op(state, op_func, hosts, *args, **kwargs):
    '''
    DEPRECATED: please use ``add_op`` with the ``hosts`` kwarg.
    '''

    # COMPAT w/ <0.4
    # TODO: remove this function

    logger.warning((
        'Use of `add_limited_op` is deprecated, '
        'please use `add_op` with the `hosts` kwarg instead.'
    ))

    if not isinstance(hosts, (list, tuple)):
        hosts = [hosts]

    # Set the limit
    state.limit_hosts = hosts

    # Add the op
    add_op(state, op_func, *args, **kwargs)

    # Remove the limit
    state.limit_hosts = []


def operation(func=None, pipeline_facts=None):
    '''
    Decorator that takes a simple module function and turn it into the internal
    operation representation that consists of a list of commands + options
    (sudo, (sudo|su)_user, env).
    '''

    # If not decorating, return function with config attached
    if func is None:
        def decorator(f):
            setattr(f, 'pipeline_facts', pipeline_facts)
            return operation(f)

        return decorator

    # Actually decorate!
    @wraps(func)
    def decorated_func(*args, **kwargs):
        # Prepare state/host
        #

        # If we're in CLI mode, there's no state/host passed down, we need to
        # use the global "pseudo" modules.
        if len(args) < 2 or not (
            isinstance(args[0], (State, PseudoModule))
            and isinstance(args[1], (Host, PseudoModule))
        ):
            state = pseudo_state._module
            host = pseudo_host._module

            if not state.active:
                return OperationMeta()

            if state.in_op:
                raise PyinfraError((
                    'Nested operation called without state/host: {0}'
                ).format(func))

        # Otherwise (API mode) we just trim off the commands
        else:
            args_copy = list(args)
            state, host = args[0], args[1]
            args = args_copy[2:]

        # Pipelining? Now we have args, we can process the argspec and prep the pipe
        if state.pipelining:
            state.pipeline_facts.process(func, decorated_func, args, kwargs)

            # Not in op? Just drop the op into state.ops_to_pipeline and return
            # here, this will be re-run once the facts are gathered.
            if not state.in_op:
                state.ops_to_pipeline.append(
                    (host.name, decorated_func, args, kwargs.copy()),
                )

        # Configure operation
        #

        # Name the operation
        names = None
        autoname = False

        # Look for a set as the first argument
        if len(args) > 0 and isinstance(args[0], set):
            names = args[0]
            args_copy = list(args)
            args = args[1:]

        # Generate an operation name if needed (Module/Operation format)
        else:
            autoname = True
            module_bits = func.__module__.split('.')
            module_name = module_bits[-1]
            names = {
                '{0}/{1}'.format(module_name.title(), func.__name__.title()),
            }

        if state.deploy_name:
            names = {
                '{0} | {1}'.format(state.deploy_name, name)
                for name in names
            }

        # Locally & globally configurable
        sudo = kwargs.pop('sudo', state.config.SUDO)
        sudo_user = kwargs.pop('sudo_user', state.config.SUDO_USER)
        su_user = kwargs.pop('su_user', state.config.SU_USER)
        ignore_errors = kwargs.pop('ignore_errors', state.config.IGNORE_ERRORS)

        # Forces serial mode for this operation (--serial for one op)
        serial = kwargs.pop('serial', False)
        # Only runs this operation once
        run_once = kwargs.pop('run_once', False)
        # Timeout on running the command
        timeout = kwargs.pop('timeout', None)
        # Get a PTY before executing commands
        get_pty = kwargs.pop('get_pty', False)
        # Whether to preserve ENVars when sudoing (eg SSH forward agent socket)
        preserve_sudo_env = kwargs.pop('preserve_sudo_env', False)

        # Callbacks
        on_success = kwargs.pop('on_success', None)
        on_error = kwargs.pop('on_error', None)

        # Limit this op to certain hosts
        hosts = kwargs.pop('hosts', False)

        # None means no hosts (see below), so use default False as None
        if hosts is False:
            hosts = None

        else:
            hosts = ensure_hosts_list(hosts)

        # Config env followed by command-level env
        env = state.config.ENV.copy()
        env.update(kwargs.pop('env', {}))

        # Get/generate a hash for this op
        op_hash = kwargs.pop('op', None)

        # If this op is being called inside another, just return here
        # (any unwanted/op-related kwargs removed above).
        if state.in_op:
            return func(state, host, *args, **kwargs) or []

        # Convert any AttrBase items (returned by host.data), see attrs.py.
        if op_hash is None:
            # Get the line number where this operation was called by looking
            # through the call stack for the first non-pyinfra line. This ensures
            # two identical operations (in terms of arguments/meta) will still
            # generate two hashes.
            frames = stack()
            line_number = None

            for frame in frames:
                if not (
                    frame[3] in ('decorated_func', 'add_op', 'add_limited_op')
                    and frame[1].endswith(path.join('pyinfra', 'api', 'operation.py'))
                ):
                    line_number = frame[0].f_lineno
                    break

            op_hash = (
                names, sudo, sudo_user, su_user, line_number,
                ignore_errors, env, args, kwargs,
            )

        op_hash = make_hash(op_hash)

        # Ensure shared (between servers) operation meta
        op_meta = state.op_meta.setdefault(op_hash, {
            'names': set(),
            'args': [],
            'su_user': su_user,
            'sudo': sudo,
            'sudo_user': sudo_user,
            'ignore_errors': ignore_errors,
            'serial': serial,
            'run_once': run_once,
            'timeout': timeout,
            'get_pty': get_pty,
            'preserve_sudo_env': preserve_sudo_env,
            'on_success': on_success,
            'on_error': on_error,
        })

        # Add any new names to the set
        op_meta['names'].update(names)

        # Attach normal args, if we're auto-naming this operation
        if autoname:
            for arg in args:
                if isinstance(arg, FunctionType):
                    arg = arg.__name__

                if arg not in op_meta['args']:
                    op_meta['args'].append(arg)

            # Attach keyword args
            for key, value in six.iteritems(kwargs):
                arg = '='.join((str(key), str(value)))
                if arg not in op_meta['args']:
                    op_meta['args'].append(arg)

        # "Run" operation
        #

        # Otherwise, flag as in-op and run it to get the commands
        state.in_op = True
        state.current_op_hash = op_hash

        # Generate actual arguments by parsing strings as jinja2 templates. This
        # means you can string format arguments w/o generating multiple
        # operations. Only affects top level operations, as must be run "in_op"
        # so facts are gathered correctly.
        actual_args = [
            get_arg_value(state, host, a)
            for a in args
        ]

        actual_kwargs = {
            key: get_arg_value(state, host, a)
            for key, a in six.iteritems(kwargs)
        }

        # Convert to list as the result may be a generator
        commands = unroll_generators(func(
            state, host,
            *actual_args,
            **actual_kwargs
        ))

        state.in_op = False
        state.current_op_hash = None

        # Make the operaton meta object for returning
        operation_meta = OperationMeta(op_hash, commands)

        # If we're pipelining, we don't actually want to add the operation as-is,
        # just collect the facts.
        if state.pipelining:
            return operation_meta

        # Add host-specific operation data to state
        #

        # Add the hash to the operational order if not already in there. To
        # ensure that deploys run as defined in the deploy file *per host* we
        # keep track of each hosts latest op hash, and use that to insert new
        # ones.
        if op_hash not in state.op_order:
            previous_op_hash = state.meta[host.name]['latest_op_hash']

            if previous_op_hash:
                index = state.op_order.index(previous_op_hash)
            else:
                index = 0

            state.op_order.insert(index + 1, op_hash)

        state.meta[host.name]['latest_op_hash'] = op_hash

        # Run once and we've already added meta for this op? Stop here.
        if run_once:
            has_run = False
            for ops in six.itervalues(state.ops):
                if op_hash in ops:
                    has_run = True
                    break

            if has_run:
                return operation_meta

        # If we're limited, stop here - *after* we've created op_meta. This
        # ensures the meta object always exists, even if no hosts actually ever
        # execute the op (due to limit or otherwise).
        if (
            (state.limit_hosts is not None and host not in state.limit_hosts)
            or (hosts is not None and host not in hosts)
        ):
            return operation_meta

        # We're doing some commands, meta/ops++
        state.meta[host.name]['ops'] += 1
        state.meta[host.name]['commands'] += len(commands)

        # Add the server-relevant commands/env to the current server
        state.ops[host.name][op_hash] = {
            'commands': commands,
            'env': env,
        }

        # Return result meta for use in deploy scripts
        return operation_meta

    decorated_func._pyinfra_op = func
    return decorated_func
