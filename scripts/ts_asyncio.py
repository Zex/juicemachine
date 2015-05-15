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

