__author__ = 'Aristarkhov Kirill Viktorovich'

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst_1 = [1, 2, 4, 0]
lst_2 = [n ** 2 for n in lst_1]


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list_1 = ['apple', 'banana', 'kiwi', 'lime', 'plum']
fruit_list_2 = ['orange', 'limon', 'kiwi', 'plum']

fruit_list = [fr for fr in fruit_list_1 if fr in fruit_list_2]


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

num_lst = [1, 4, 56, 67, 234, -78, 0, -25, 7, -38, 99]
num_result = [nam for nam in num_lst if (nam % 3 == 0) and (nam > 0) and (nam % 4 != 0)]
