
__author__ = 'Aristarkhov Kirill Viktorovich'


#EASY-NORMAL
# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника,
# если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def draw_point(self):
        return f"({self.x},{self.y})"

    def _move(self, dx, dy):
        return self.x + dx, self.y + dy

    def get_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Triangle:

    p1 = Point()
    p2 = Point()
    p3 = Point()

    def __init__(self, x1, y1, x2, y2, x3, y3):
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)


    def draw_triangle(self):
        p1.draw_point()
        p2.draw_point()
        p3.draw_point()


    def get_square(self):
        return abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2


    def get_perimeter(self):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0,5 + ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0,5 + \
               ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0,5
