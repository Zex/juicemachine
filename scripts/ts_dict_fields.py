    class Users(dict):

        _field = [
                'name',
                ]

        @property
        def name(self):
            return self.__getitem__('name')
        
        @name.setter
        def name(self, entry):
            self.__setitem__('name', entry)

        @property
        def cards(self):
            return self.__getitem__('cards')
        
        @cards.setter
        def cards(self, entry):
            self.__setitem__('cards', entry)

    u = Users()
    u.name=2345678
    print('1',u.name)
    print('2',u['name'])
    print(u)

    x = Users()
    x.name='dfghj'
    print('1',x.name)
    print('2',x['name'])
    print(x)
    
    x.cards = ['111','222',]
    print(x)
    print(u)
