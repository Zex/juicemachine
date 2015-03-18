#!/usr/bin/python3

import ctypes as ct

DUMMY_LIB_PATH = 'libdummy.so.0.1.0'

class Endec(object):
    """
    create_unicode_buffer(aString) -> character array
    create_unicode_buffer(anInteger) -> character array
    create_unicode_buffer(aString, anInteger) -> character array
    
    create_string_buffer(aString) -> character array  
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aString, anInteger) -> character array
    """

    self._libdummy = ct.cdll.LoadLibrary(DUMMY_LIB_PATH)

    def __init__(self):

        self._libdummy.setCountdown(999)

    def __del__(self):

        self._libdummy.setCountdown(0)

    def enable(self, in_buffer):

        if not isinstance(in_buffer, str):
            raise TypeError('string type required')

        addr   = ct.c_buffer(in_buffer.encode())
        ret    = ct.c_buffer(''.encode(), 1024)
        length = ct.pointer(ct.c_uint(0))
        self._libdummy.enable_slayer(addr, len(in_buffer), ret, length)

        return (ret.value, length.contents)

    def disable(self, in_buffer):
       
        if not isinstance(in_buffer, bytes):
            raise TypeError('bytes type required')

        addr   = ct.c_buffer(in_buffer)
        ret    = ct.c_buffer(''.encode(), 1024)
        length = ct.pointer(ct.c_uint(0))
        self._libdummy.disable_slayer(addr, len(in_buffer), ret, length)
        
        return (ret.value, length.contents)

