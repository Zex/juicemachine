#!/usr/bin/env python3


import asyncio as aio

LOG_PREF    = "LOG>"

def LOG(*msg):
    print(LOG_PREF, msg)

@aio.coroutine
def read_backend():
    LOG('READING BACKEND ...')


loop = aio.get_event_loop()
loop.run_until_complete(read_backend())
loop.close()

aio.start_server(loop)

#['ALL_COMPLETED', 'AbstractChildWatcher', 'AbstractEventLoop', 'AbstractEventLoopPolicy', 'AbstractServer', 'BaseEventLoop', 'BaseProtocol', 'BaseTransport', 'BoundedSemaphore', 'CancelledError', 'Condition', 'DatagramProtocol', 'DatagramTransport', 'DefaultEventLoopPolicy', 'Event', 'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'FastChildWatcher', 'Future', 'Handle', 'IncompleteReadError', 'InvalidStateError', 'JoinableQueue', 'LifoQueue', 'Lock', 'PriorityQueue', 'Protocol', 'Queue', 'QueueEmpty', 'QueueFull', 'ReadTransport', 'SafeChildWatcher', 'SelectorEventLoop', 'Semaphore', 'StreamReader', 'StreamReaderProtocol', 'StreamWriter', 'SubprocessProtocol', 'SubprocessTransport', 'Task', 'TimeoutError', 'TimerHandle', 'Transport', 'WriteTransport', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'as_completed', 'async', 'base_events', 'base_subprocess', 'constants', 'coroutine', 'coroutines', 'create_subprocess_exec', 'create_subprocess_shell', 'events', 'futures', 'gather', 'get_child_watcher', 'get_event_loop', 'get_event_loop_policy', 'iscoroutine', 'iscoroutinefunction', 'locks', 'log', 'new_event_loop', 'open_connection', 'open_unix_connection', 'protocols', 'queues', 'selector_events', 'selectors', 'set_child_watcher', 'set_event_loop', 'set_event_loop_policy', 'shield', 'sleep', 'sslproto', 'start_server', 'start_unix_server', 'streams', 'subprocess', 'sys', 'tasks', 'transports', 'unix_events', 'wait', 'wait_for', 'wrap_future']
#['ALL_COMPLETED', 'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'Task', '_GatheringFuture', '_PY34', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_release_waiter', '_wait', 'as_completed', 'async', 'concurrent', 'coroutine', 'coroutines', 'events', 'functools', 'futures', 'gather', 'inspect', 'linecache', 'shield', 'sleep', 'sys', 'traceback', 'wait', 'wait_for', 'weakref']
