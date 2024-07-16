from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def say_smth(self):
        raise NotImplementedError

    @abstractmethod
    def walk(self):
        raise NotImplementedError

    def say_hi(self):
        print('Hi')


class Cat(Animal):

    def say_smth(self):
        print('Mew')

    def walk(self):
        print('Mew')

    # @abstractmethod
    # def walk(self):
    #     raise NotImplementedError


cat = Cat()

cat.say_smth()
cat.say_hi()