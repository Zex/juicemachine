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

    def dump(self, path=None):
        raise NotImplementedError('Unimplemented')

    def load(self, path=None):
        raise NotImplementedError('Unimplemented')

if __name__ == '__main__':

    pass


