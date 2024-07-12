
class Cat:

    name = 'cat'

    def sey_mew(self):

        def say_ahh():
            print(f'ahh, {self.name}')

        say_ahh()

        print(f'mew, {self.name}')


c = Cat()
c.sey_mew()