# class MyIterator:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.start = 0
#             self.end = args[0]
#             self.step = 1
#         if len(args) == 2:
#             self.start = args[0]
#             self.end = args[1]
#             self.step = 1
#         if len(args) == 2:
#             self.start = args[0]
#             self.end = args[1]
#             self.step = args[2]
#
#         self.__current = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__current < self.end:
#             self.__current += self.step
#             return self.__current
#         else:
#             raise StopIteration



# my_iterator = MyIterator(50)
#
# i_obj = iter(my_iterator)
# print(next(i_obj))
# print(next(i_obj))
#
# for num in my_iterator:
#     print(num)

class MyIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_num:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iterator = MyIterator(5)
i_obj = iter(my_iterator)  # == my_iterator.__iter__()

for num in my_iterator:
    print(num)


