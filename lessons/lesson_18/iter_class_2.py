class Student:

    def __init__(self, name, math=20, art=30, music=40):

        self.name = name

        self.math = math
        self.art = art
        self.music = music

        self.__returned_values = []
        self.__scores = {'math': self.math, 'art': self.art, 'music': self.music}


    def __iter__(self):
        return self

    def __next__(self):
        for k in self.__scores:
            if k not in self.__returned_values:
                self.__returned_values.append(k)
                return {k: self.__scores[k]}  # set = {1, 2, 3, 4} vs dict = {1:2, 3:4}
        raise StopIteration


st = Student("Alex")

for score in st:
    print(score)