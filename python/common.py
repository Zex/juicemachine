#!/usr/bin/python
# common.py
#
# Common data structure definitions for juicemachine
#
# Author: Zex <top_zlynch@yahoo.com>
#

from checker import *

class CommonJM(object):
    """
    Common data structure definitions for juicemachine
    """
    __slots__ = [
        ]
        
    def __init__(self):
        pass

    @string_chk
    def name(self): pass

    @string_chk
    def identity(self): pass
    
    @integer_chk
    def count(self): pass

    def dump(self, path=None):
        raise NotImplementedError('Unimplemented')

    def load(self, path=None):
        raise NotImplementedError('Unimplemented')

if __name__ == '__main__':

    pass


