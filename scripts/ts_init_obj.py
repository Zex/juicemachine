class O:

    _o = 123

    def __init__(self):

        pass

class A:
    """
    def __init__(self):
        self._num = O()

    <__main__.A object at 0x7fa75f32a5c0> <__main__.A object at 0x7fa75f32a6a0>
    <__main__.O object at 0x7fa75f32a630> <__main__.O object at 0x7fa75f32a6d8>

    ==> `_num` of the two A instances are different objects

    _num = O()

    def __init__(self):
        pass

    <__main__.A object at 0x7fa9d5d5e5c0> <__main__.A object at 0x7fa9d5d5e630>
    <__main__.O object at 0x7fa9d5d5e550> <__main__.O object at 0x7fa9d5d5e550>

    ==> `_num` of the two A instances are the same objects
    """

    _num = O()

    def __init__(self):

        pass

    def __eq__(self, b):
        pass

a = A()
b = A()

print(a, b)
print(a._num, b._num)
