#!/usr/bin/env python3

class A(dict):

    _fields = [
        'hello',
        ]

    @property
    def hello(self):
         return self.get('hello')

    @hello.setter
    def hello(self, entry):
         self.__setitem__('hello', entry)

class whole_member(object):
    """object
    """
    mem_a = A()
    """string
    """
    name = 'hello, name'
    """list of dict
    """
    groups = []
    """dict of dict
    """
    dod = {}

    _fields = [
            'mem_a',
            'name',
            'groups',
            'dod',
           ]

    def __iter__(self):
        """Project each member to a value buffer
        when being access"""

        buf = dict.copy({x:getattr(self, x) for x in self._fields})

        buf['mem_a'] = dict.copy(self.mem_a)

        buf['groups'] = list.copy(self.groups)

        for ind in range(len(self.groups)):
           buf['groups'][ind] = dict.copy(self.groups[ind])

        buf['dod'] = dict.copy(self.dod)

        for k, v in self.dod.items():
           buf['dod'][k] = dict.copy(self.dod[k])

        for k,v in buf.items(): yield(k,v)

who_1 = whole_member()

print('----------------init original object----------------------')
who_1.mem_a.hello = 'hello,1'

who_1.groups.append(A())
who_1.groups.append(A())

who_1.groups[0].hello = 'hello, group 1'
who_1.groups[1].hello = 'hello, group 2'

who_1.dod = {
    'a1':A(),
    'a2':A(),
    }
who_1.dod['a1'].hello = 'hello, dod 1'
who_1.dod['a2'].hello = 'hello, dod 2'
print(dict(who_1))

print('-----------------------init buf---------------------------')
buf = dict(who_1)

print('buf', buf)
print('----------------------------IDs---------------------------')
print('buf', id(buf), 'who_1',id(who_1))
print('buf', id(buf), 'who_1',id(who_1))
print('buf[mem_a]', id(buf['mem_a']), 'who_1.mem_a',id(who_1.mem_a))
print('buf[groups]', id(buf['groups']), 'who_1.groups',id(who_1.groups))
print('buf[dod]', id(buf['dod']), 'who_1.dod',id(who_1.dod))

print('------------------------hacking---------------------------')
buf['name'] = 'name of buf'
buf['mem_a']['hello'] = 'hello, buf'
buf['groups'][0]['hello'] = 'hello, group buf'
buf['dod']['a1']['hello'] = 'hello, dod buf'

print('buf', buf)
print('----------------------------+++---------------------------')
print('who_1.name', who_1.name)
print('who_1.mem_a', who_1.mem_a)
print('who_1.groups', who_1.groups)
print('who_1.dod', who_1.dod)

