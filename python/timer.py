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
        
        self.__intv = intv
        self.__func = func
        self.__running = True

        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self, *args):

        while self.__running and self.__func:

            with threading.Lock() as l:
                threading._sleep(self.__intv)
                self.__func(*args)
    
    def cancel(self):

        print('cancel ...')
        self.__running = False

if __name__ == '__main__':

    tm = Timer(2, timer_cb)
    tm.run()

