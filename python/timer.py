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

class Dumper(threading.Thread):

    def __init__(self, intv=None, func=None, *args):

        self.intv = intv
        self.func = func
        self.__running = True

    def run(self, *args):

        while self.__running and self.func:

            self.func(*args)

    def cancel(self):

        self.__running = False

if __name__ == '__main__':

    Timer = Dumper(2, timer_cb)
    Timer.run()

