import math


class DoubleList:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __iter__(self):
        for v in self.list1:
            yield v
        for v in self.list2:
            yield v

    def __len__(self):
        return len(self.list1) + len(self.list2)

    def __getitem__(self, i):
        if i < len(self.list1):
            return self.list1[i]
        else:
            return self.list2[i-len(self.list1)]



a = [1, 2, 3]
b = ['a', 'b', 'c']
dl = DoubleList(a, b)
# for v in dl:
#     print(v)


for i in range(len(dl)):
    print(dl[i])

print()
print()
print()
print()
print()
print()
print()
print()








#
#
# class PointPriv:
#     def __init__(self, x, y):
#         self.__x = x  # use two underscores to denote a private variable
#         self.__y = y
#
#     def get_xy(self):
#         return self.__x, self.__y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, y):
#         self.__y = y
#
#
# p1 = PointPriv(5, 2)
#
# # p1.x += 5
# p1.set_x(p1.get_x()+5)
#
#
#
#
#
# x, y = p1.get_xy()
#
#
#
# def changepoint(p):
#     p = PointPriv(5, 3)
#
#













class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):  # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    def __iter__(self):
        yield self.x
        yield self.y




p3 = Point()
p1 = Point(5, 2)


for v in p1:
    print(v)
print()



p2 = Point(8, 4)
dist = p1.distance(p2)  # or p2.distance(p1), either works
#dist = Point.distance(p1, p2)

print(Point)
c = Point
p3 = c(5, 2)
print(p3)







print(dist)
# similar to how we can call methods of the str class
s = 'hello world'
print(s.split(' '))