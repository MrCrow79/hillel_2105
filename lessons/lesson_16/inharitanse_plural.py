class BaseAnimals:  # ромбовидне наслідування

    @staticmethod
    def walk():
        print('I\'m walking BaseAnimals')

class Animals(BaseAnimals):

    @staticmethod
    def walk():
        print('I\'m walking Animals')


class Bird(BaseAnimals):

    @staticmethod
    def walk():
        print('I\'m walking Bird')


class Horse(Animals):

    @staticmethod
    def run():
        print('I\'m running')


class Eagle(Bird):

    @staticmethod
    def fly():
        print('I\'m flying')

    @staticmethod
    def walk():
        print('I\'m walking Eagle')


class Pegasus(Horse, Eagle):  # Horse -> Horse Father(Animal) -> Eagle -> Eagle Father(Bird)
    pass


class Users():

    def get_users(self):
        pass

class Lessons():

    def get_lessons(self):
        pass

#
# class UsersAtLessons(Users, Lessons):
#
#     def calculate_volumes(self):
#         users = self.get_users()
#         lessons = self.get_lessons()


# class UsersAtLessons:
#
#     def __init__(self):
#         self.user = Users()
#         self.lesson = Lessons()
#
#     def calculate_volumes(self):
#         users = self.user.get_users()
#         lessons = self.lesson.get_lessons()
#         ...


pegasus = Pegasus()

pegasus.run()
pegasus.fly()
pegasus.walk()

print(Pegasus.mro())