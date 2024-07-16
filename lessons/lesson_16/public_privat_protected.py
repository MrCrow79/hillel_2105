#  public
#  protected
#  private

import random


class BaseGame:
    _greeting = 'Hello from BaseGame'

    @classmethod
    def print_greeting(cls):
       return cls._greeting


class Game(BaseGame):
    _greeting = 'Hello from Game'

    # dice

    def __init__(self, max_tries):
        self.max_tries = max_tries  # public attribute
        self._tries_left = max_tries  # protected attribute
        self.__extra_roll = False  #  private  attribute
        self.__win_number = random.choice(range(1, 7))  #  private attribute
        self.__is_winner = None  #  private  attribute

    def roll_dice(self):  # public method

        if self.__is_winner is False:
            print('You are the loser')
            return

        if self.__is_winner is True:
            print('You already win')
            return

        number = random.choice(range(1, 7))  # 1,2,3,4,5,6
        if self._tries_left < 3:
            self.__extra_roll = True

        if self.__extra_roll is True and number != self.__win_number:
            number = random.choice(range(1, 7))

        if number == self.__win_number:
            self.__is_winner = True

        if self.__is_winner:
            print('You are the winner')

        self._tries_left -= 1

        if self._tries_left == 0:
            self.__is_winner = False


class EasyGame(Game):
    __greeting = 'asdasd'

    def __init__(self):
        super().__init__(3)

    def roll_dice(self):

        if self.__is_winner is False:
            print('You are the loser')
            return

        if self.__is_winner is True:
            print('You already win')
            return

        if self._tries_left == 0:
            self.__is_winner = False
            print('Game over. You lose')


game = Game(6)
#
# game.print_greeting()
# game.roll_dice()
# print(game.max_tries)
# print(game._tries_left)

easy_game = EasyGame()
easy_game.__class__._greeting = 'Hello from Instance'
x = easy_game.print_greeting()
print(x)

print(easy_game._tries_left)
