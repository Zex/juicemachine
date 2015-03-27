#!/usr/bin/env python
#
# checker.py
# Restrictions on data fields
#
# Author: Yun Li <Yun_Li1@DellTeam.com>
#
#
from basic import *
   

class Checker(property):
    """
    Schema related restrictions

    @ilen   length of one item, 0 for unlimited
    @nr     number of items, 0 for unlimited 
    @tlen   total length of a fields, 0 for unlimited
    """
    _value = None
    __ilen = 0
    __nr   = 0
    __tlen = __ilen * __nr

    @property
    def ilen(self): return self.__ilen

    @ilen.setter
    def ilen(self, entry):
        self.__ilen = entry
        self.tlen = self.ilen * self.nr

    @property
    def nr(self): return self.__nr

    @nr.setter
    def nr(self, entry):
        self.__nr = entry
        self.tlen = self.ilen * self.nr

    @property
    def tlen(self): return self.__tlen

    @tlen.setter
    def tlen(self, entry):
        self.__tlen = entry

    def __init__(self, func):

        self.ilen = 0
        self.tlen = 0

    def __get__(self, obj, cls):
        return self._value

    def __set__(self, obj, entry):

        self._value = entry

#    def __setattr__(self, name, entry):
#
#        property.__setattr__(self, name, entry)
#
#        if name in ['ilen', 'nr']:
#            self.tlen = self.ilen * self.nr

class list_chk(Checker):

    _value = []

    def __set__(self, obj, entry):

        if not isinstance(entry, list) and entry is not None:
            raise TypeError('list type required')

        if self.nr > 0 and len(entry) > self.nr:
            raise ValueError('too much items')

        if entry is not None:
            self._value = entry

class string_chk(Checker):

    _value = str()

    def __set__(self, obj, entry):

        if entry is None or entry == '':
            self._value = ''
            return

        if not isinstance(entry, str):
            raise TypeError('string type required')

        if self.tlen > 0 and len(entry) > self.tlen:
            raise ValueError('value length exceeded')

        self._value = entry

class integer_chk(Checker):

    _value = int()

    def __set__(self, obj, entry):

        if entry is None: return

        if not isinstance(entry, int):
            raise TypeError('integer type required')

        self._value = entry

class boolean_chk(Checker):

    _value = bool()

    def __set__(self, obj, entry):

        if entry is None: return

        if not isinstance(entry, bool):
            raise TypeError('boolean value required')

        self._value = entry

class map_chk(Checker):

    _value = {}

    def __set__(self, obj, entry):

        if entry is None: return

        if not isinstance(entry, dict):
            raise TypeError('list required')

        self._value = entry

class list_of_string_chk(list_chk):

    def __set__(self, obj, entry):
        
        super(list_of_string_chk, self).__set__(obj, entry)

        for e in entry:
            if not isinstance(e, str):
                raise TypeError('list of string required')

        if entry is not None:
            self._value = entry

class dotted_ip_chk(string_chk):

    reobj = re.compile('^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')

    ilen = 15
    nr   = 1

    def __set__(self, obj, entry):

        super(dotted_ip_chk, self).__set__(obj, entry)

        if len(entry) and not self.reobj.match(entry):
            raise ValueError('Dotted string required')

        self._value = entry

class mac_chk(string_chk):

    reobj = re.compile('^([0-9A-Fa-f]{2}[.:-]{0,1}){6}$')
    ilen  = 17
    nr    = 1

    def __set__(self, obj, entry):

        super(mac_chk, self).__set__(obj, entry)

        if len(entry) and not self.reobj.match(entry):
            raise ValueError('Colon delimited string required')

        self._value = entry

class dummy_chk(list_chk):
    """
    type('usersettings_chk', (list_chk,), {'ilen':1, 'nr':2})
    """
    def __init__(self, func):

        self.ilen = 1
        self.nr = 5
"""
from cipher_helper import CiHelper

class passwd_chk(string_chk):

    __ci = CiHelper

    def __init__(self, func):
        
        self._value = ''

    def __set__(self, obj, entry):

        string_chk(None).__set__(obj, entry)

        try:
            b64.b64decode(entry, validate=True)
            self._value = entry
        except b64.binascii.Error:
            self._value = self.__ci.enc(entry)[0]

    def __get__(self, obj, cls):

        return self.__ci.dec(self._value)[0]

"""
