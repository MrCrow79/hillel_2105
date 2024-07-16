class DiceGame:

    def __init__(self):
        self.__max_tries = 10  # == self._DiceGame__max_tries
        self.__left_tries = 10  # == self._DiceGame__left_tries

    def roll(self):
        if self.__left_tries > 0:
            self.__left_tries -= 1
        else:
            print('You have no tries')

    @property
    def left_tries(self):
        return self.__left_tries

    @left_tries.setter
    def left_tries(self, value):
        if value > self.__left_tries:
            return
        else:
            self.__left_tries = value
        return self.__left_tries

    # getter
    def get_left_tries(self):
        return self.__left_tries

    # setter
    def set_left_tries(self, value):
        if value > self.__left_tries:
            return
        else:
            self.__left_tries = value
        return self.__left_tries


game = DiceGame()

print(game.get_left_tries())
print(game.left_tries)
game.left_tries = 50
print(game.left_tries)
game.left_tries = 3
print(game.left_tries)
game.roll()
# print(game.get_left_tries())
# game.set_left_tries(100)
# print(game.get_left_tries())
# game.set_left_tries(1)
# print(game.get_left_tries())
