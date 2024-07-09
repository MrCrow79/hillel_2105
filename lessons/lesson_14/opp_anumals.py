class Lion:

    def run(self):
        print('I\'m running really fast')

    def eat(self):
        print('I\'m eating')

    def hunt(self):
        print('Hunting in progress')

    def live(self):
        self.run()
        self.eat()
        self.hunt()


class Cat:

    def __init__(self, cats_number=1):
        self.cats_number = cats_number

    def run(self):
        print('I\'m running really fast')

    def eat(self):
        print('I\'m eating like a cat')

    def hunt(self):
        print('Hunting in progress')

    def live(self):
        self.run()
        self.hunt()
        self.eat()

    def __len__(self):
        return self.cats_number


lion = Lion()
cat = Cat()
#
lion.live()
cat.live()

print(5 + 8)
print('Cool' + ' stuff')

print(len('asdasd'))  # 'asdasd'.__len__()
print(len([1, 2, 3]))

print(len(cat))
cat.cats_number = 10
print(len(cat))

lion.run()
lion.hunt()
lion.eat()
