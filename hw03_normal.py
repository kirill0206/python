__author__ = 'Aristarkhov Kirill Viktorovich'

import random
#NORMAL
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a = [1, 1]
    while len(a) < m:
        a.append(a[-1] + a[-2])
    return a[n-1:m]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list) -> list:
    if len(origin_list) <= 1:
        return origin_list
    else:
        q = random.choice(origin_list)
    l_list = [num for num in origin_list if num < q]
    e_list = [q] * origin_list.count(q)
    b_list = [num for num in origin_list if num > q]
    return sort_to_max(l_list) + e_list + sort_to_max(b_list)


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
