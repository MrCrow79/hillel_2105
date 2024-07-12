class Student:  # class Student(type)

    def __init__(self, name, student_id, rating):
        self.name = name
        self.student_id = student_id
        self.rating = rating

    def __str__(self) -> str:  # str(inst)
        return f'{self.name} with id={self.student_id} and rating = {self.rating}'

    def __add__(self, other):  # +
        return self.rating + other

    def __len__(self):
        return 1

    def __repr__(self) -> str:
        return f'Student(\'{self.name}\', {self.student_id}, {self.rating})'


ivan = Student('Ivan', 10, 75)
str(ivan)  # == ivan.__str__()
print(ivan)

# print(ivan + '  asdasdasdstr')  # == ivan.__add__('  asdasdasdstr')
print(len(ivan))  # ivan.__len__()

print(ivan.__repr__())
ivan.rating = ivan.rating + 10
print(ivan.__repr__())

debug_ivan = Student('Ivan', 10, 85)



