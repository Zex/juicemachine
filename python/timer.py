#! /usr/bin/python
# Timer.py

import threading

def timer_cb():
    print('timer_cb ...')
"""
    threading.Timer(3.0, timer_cb).run()

obj = threading.Timer(3.0, timer_cb)
obj.run()
"""

class Timer(threading.Thread):

    def __init__(self, intv=None, func=None, *args):
        
        self._intv = intv
        self._func = func
        self._running = True

        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self, *args):

        while self._running and self._func:

            threading._sleep(self._intv)

            with threading.RLock() as l:
                self._func(*args)
    
    def cancel(self):

        print('cancel ...')
        self._running = False

if __name__ == '__main__':

    tm = Timer(2, timer_cb)
    tm.run()

