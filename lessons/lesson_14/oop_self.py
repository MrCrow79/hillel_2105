class Dog:  # class name

    def __init__(self, base_name, base_color, *args, base_age=8, nickname=None, **kwargs):   # magic method, initialization
        self.name = base_name  # attribute
        self.color = base_color  # attribute
        self.age = base_age  # attribute
        self.nickname = nickname  # attribute
        self.additional_attributes = args  # attribute: tuple with values
        self.additional_kye_attributes = kwargs  # attribute: dict with values

    def say_waf(self):  # method
        print('waf')

    def sat_name(self, new_name):  # method
        self.name = new_name

    def say_your_name(self):  # method
        print(f'my name is {self.name}')


my_black_dog = Dog('Albert', 'Black', nickname='Good boy')  # call method __init__()
my_white_dog = Dog('Jack', 'White', 1)  # call method __init__()

my_green_dog = Dog('Scooby', 'Green',
                   'attribute_1', 'attribute_2', 'asdasdasd', 'attribute_1',
                   nickname='Good boy',
                   key_attr='kye_attr_1', key_attr2='kye_attr_1', asd='kye_attr_1')  # call method __init__()

my_black_dog.say_your_name()
my_white_dog.say_your_name()
my_green_dog.say_your_name()
