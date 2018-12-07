
__author__ = 'Aristarkhov Kirill Viktorovich'

# EASY-NORMAL
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

#    p1 = Point()
#    p2 = Point()
#    p3 = Point()

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if (x3 * (y2 - y1) - y3 * (x2 - x1)) == (x1 * y2 - x2 * y1):
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            p3 = Point(x3, y3)
        else:
            print("Треугольник с такими вершинами нельзя создать")
            exit(1)

    def draw_triangle(self):
        return f"({self.p1.x},{self.p1.y},{self.p2.x},{self.p2.y},{self.p3.x},{self.p3.y})"

    def get_square(self):
        return abs((self.p1.x - self.p3.x) * (self.p2.y - self.p3.y) - (self.p2.x - self.p3.x) *
                   (self.p1.y - self.p3.y)) / 2

    def get_perimeter(self):
        return ((self.p1.x - self.p2.x) ** 2 + (self.p1.y - self.p2.y) ** 2) ** 0.5 + \
               ((self.p2.x - self.p3.x) ** 2 + (self.p2.y - self.p3.y) ** 2) ** 0.5 + \
               ((self.p3.x - self.p1.x) ** 2 + (self.p3.y - self.p1.y) ** 2) ** 0.5


# test = Triangle(1, 1, 2, 2, 3, 3)
# print(test.draw_triangle())

test1 = Point(1, 2)
print(test1.draw_point())
