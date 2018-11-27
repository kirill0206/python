
__author__ = 'Aristarkhov Kirill Viktorovich'

import random


# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


f = open("number.txt", "a", encoding="utf-8")
max_len = [0, 0]    # type: [int, int]
current_len = 0     # type: int
prev_n = -1         # type: int

for i in range(2500):
    n = random.randint(0, 9)
    f.write(str(n))
    if n == prev_n:
        current_len += 1
        if current_len > max_len[0]:
            max_len[0] = current_len
            max_len[1] = n
    else:
        current_len = 1
    prev_n = n

f.close()

print(str(max_len[1]) * max_len[0])

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте,
# остальные элементы тоже рандомные.
# Пользователь вводит размер


n = int(input("Введите размер: "))
# get random matrix
matrix = [[random.randint(1, 99) for i in range(n)] for j in range(n)]
# set 0 to random position in each lines
for i in range(n):
    j = random.randint(0, n-1)
    matrix[i][j] = 0
# print matrix
for row in matrix:
    for cel in row:
        print('{:4d}'.format(cel), end=" ")
    print("")

print("==============================")
