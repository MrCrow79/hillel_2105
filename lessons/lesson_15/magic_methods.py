class Student:

    def __init__(self, name, student_id, rating, am_average=None):
        self.name = name
        self.student_id = student_id
        self.rating = rating
        self.am_average = am_average

    def compare(self, st2) -> bool:
        if self.rating > st2.rating:
            return True
        if self.rating <= st2.rating:
            return False

    def __gt__(self, st2):  # grate, >

        if self.am_average is None:
            am_average_local = 0
        else:
            am_average_local = self.am_average

        if st2.am_average is None:
            am_average_local_s2 = 0
        else:
            am_average_local_s2 = st2.am_average

        diff = self.rating + am_average_local - st2.rating + am_average_local_s2
        print(f'Diff is {diff}')

        if self.rating + am_average_local > st2.rating + am_average_local_s2:
            return True
        if self.rating + am_average_local <= st2.rating + am_average_local_s2:
            return False


class StudentMath(Student):
    pass


class StudentPhil(Student):

    def __init__(self, name, student_id, rating, am_average: int):
        super().__init__(name, student_id, rating, am_average)

    def compare(self, st2) -> bool:
        if self.rating + self.am_average > st2.rating + st2.am_average:
            return True
        if self.rating + self.am_average <= st2.rating + st2.am_average:
            return False


    # def __lt__(self, other):  # less, <
    # def __ge__(self, other):  # >=
    # def __le__(self, other):  # less, <=
    # __len__
    # __eq__ #  equal =




ivan = StudentMath('Ivan', 10, 75)
petro = StudentPhil('Petro', 11, 77, am_average=80)
vasyl = StudentPhil('Vasyl', 11, 77, am_average=81)

print(petro > ivan)




