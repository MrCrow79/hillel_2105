

class BlackDog:  # class name

    color = 'Black'  # attribute
    name = 'Jack'

    def say_waf(self):  # method
        print('waf')

    def set_name(self, new_name):
        self.name = new_name


my_dog = BlackDog()  # instance
my_second_dog = BlackDog()

print(my_dog.name)

my_dog.set_name('Albert')

print(my_dog.name)
print(my_second_dog.name)
pass


my_dog.say_waf()
my_second_dog.say_waf()

print(id(my_dog))
print(id(my_second_dog))



