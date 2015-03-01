#!/usr/bin/python
# common.py
#
# Common data structure definitions for juicemachine
#
# Author: Zex <top_zlynch@yahoo.com>
#

class string_ty(property):

    __value = ''

    def __set__(self, name, entry):

        if not isinstance(entry, str):
            raise TypeError('string value is required')

        self.__value = entry

    def __get__(self, *args):
        return self.__value

class integer_ty(property):

    __value = int()

    def __set__(self, name, entry):

        if not isinstance(entry, int):
            raise TypeError('integer value is required')

        self.__value = entry

    def __get__(self, *args):
        return self.__value

class CommonJM(object):
    """
    Common data structure definitions for juicemachine
    """
    __slots__ = [
        ]
        
    def __init__(self):
        pass

    @string_ty
    def name(self): pass

    @string_ty
    def identity(self): pass
    
    @integer_ty
    def count(self): pass

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

    try:
        c.dummy = 568
    except Exception as e:
        print(e)
    print('id:',c.identity)
    c.identity = 'kjhgfd'
    print('id:',c.identity)
    print('count:',c.count)
    print(type(c.count))
    c.count = 1234567
    print('count:',c.count)


if __name__ == '__main__':

    selftest()


