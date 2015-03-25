#!/usr/bin/python
# common.py
#
# Common data structure definitions for juicemachine
#
# Author: Zex <top_zlynch@yahoo.com>
#
# Shared port for communication amount jms
#
#   ...
#    jm1 = jm_port_1()
#    jm2 = jm_port_2()
#
#    print(jm1.jm_shared_port)
#    print(jm2.jm_shared_port)
#
#    jm1.jm_shared_port = "blue-port-7"
#
#    jm1.print_name()
#    jm2.print_name()
#   ...
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

class __juicemachine_base__:

    @string_chk
    def jm_shared_port(self): pass

    def print_name(self):
        raise NotImplementedError('Unimplemented')

class jm_port_1(__juicemachine_base__):

    def __init__(self):
        self.jm_shared_port = 'jm_port_1'

    def print_name(self):
        print("name: jm-1 @", self.jm_shared_port)

class jm_port_2(__juicemachine_base__):

    def __init__(self):
        self.jm_shared_port = 'jm_port_2'
    
    def print_name(self):
        print("name: jm-2 @", self.jm_shared_port)




