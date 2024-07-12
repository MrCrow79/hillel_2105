class Romb:

    def __init__(self, a, b, name='just Romb'):
        self.a = a
        self.b = b
        self.name = name

    def __setattr__(self, key, value):  # set attribute
        if key in ('a', 'b'):  # if key == 'a' OR key == 'b'
            if type(value) in (int, float) and value > 0:  # (type(value) is int OR type(value) is float) AND value > 0
                super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    def __getattr__(self, item):  # get attribute

        if item in self.__dict__:  # dict with all attributes of instance
            return item
        else:
            print(f'calling {item} attribute but it\'s not exist')
            return None

    def __str__(self):
        return f'{self.name}: {self.a}, {self.b}'

    def __del__(self):
        print(f'Object was deleted {str(self)}')

    def square(self):
        return 2*self.a * 2*self.b

    def perimeter(self):
        return 2*self.a + 2*self.b


    # def square(self):
    #     if self._check_attributes():
    #         return 2*self.a * 2*self.b
    #     else:
    #         return 0
    #
    # def perimeter(self):
    #     if self._check_attributes():
    #         return 2*self.a + 2*self.b
    #     else:
    #         return 0
    #
    #
    # def _check_attributes(self):
    #     if type(self.a) in (int, float) and type(self.b) in (int, float):
    #
    #         if self.a >= 0 and self.b >= 0:
    #             return True
    #
    #     return False




if __name__ == '__main__':
    r1 = Romb(2,3)
    r2 = r1
    print(r1.square())
    print(r1.perimeter())

    r1.a = -5  # == r1.__setattr__('a', -5)
    r1.c = -5
    print(r1.square())
    r1.a = 'a'

    r1.b = 50

    print(r1.square())
    print(r1.a)  # == print(ra.__getattr__('a'))
    print(r1.b)
    print(r1.c)
    print(r1.__dict__)
    print(r1.aaaaa)

    # del r1