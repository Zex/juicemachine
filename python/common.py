#!/usr/bin/python
# common.py
#
# Common data structure definitions for juicemachine
#
# Author: Zex <top_zlynch@yahoo.com>
#

class CommonJM(object):
    """
    Common data structure definitions for juicemachine
    """
    __slots__ = [
        '__name',
        ]
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, entry):
        if not isinstance(entry, str):
            raise TypeError('string value is required')
        self.__name = entry

def selftest():

    c = CommonJM()
    print(c.name)
    c.name = 'qwerty'
    print(c.name)
    try:
        c.name = 2345
        print(c.name)
    except Exception as e:
        print(e)

    c.dummy = 568

if __name__ == '__main__':

    selftest()

