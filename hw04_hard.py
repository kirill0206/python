
__author__ = 'Aristarkhov Kirill Viktorovich'

import random

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков.
# Имеется ли хотя бы один просвет по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.


def check_lines(i, j):

    result = []

    # check in Z scale
    if 1 in matr[i][j]:
        result.append([i, j, 0])

    # check in Y scale
    condition = True
    for x in range(len(matrix)):
        if matrix[i][x][j] != 0:
            condition = False
    if condition:
        result.append([i, 0, j])

    # check in X scale
    condition = True
    for x in range(len(matrix)):
        if matrix[x][i][j] != 0:
            condition = False
    if condition:
        result.append([0, i, j])
    return result


n = 3
matrix = [[[random.randint(0, 1) for i in range(n)] for j in range(n)] for k in range(n)]
for i in range(n):
    for j in range(n):
        lines = check_lines(i, j)
        if len(lines) != 0:
            for k in len(lines):
                print("Координаты просвета:\n x = {:d}\n y = {:d}\n z = {:d}".format(lines[k][0], lines[k][1], lines[k][2]))


# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

def get_key(value):
    for k, v in dict1.items():
        if v == value:
            return k


def get_passwds():
    for line in string.split("\n"):
        pass_word = line.split(";")[1]
        count = dict1.get(pass_word)
        dict1.update({pass_word: 1}) if count is None else dict1.update({pass_word: (count + 1)})


with open("pwd.txt", "r", encoding="utf-8") as f:
    string = (f.read().strip())

dict1 = dict()      # password : count

get_passwds()

pass_count = sorted(dict1.values())

for i in range(10):
    print(str(i+1) + get_key(pass_count[-1 - i]))

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами

# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5


def get_matrix(n_matr):
    return [[0 for i in range(n_matr)] for j in range(n_matr)]


def change_dir():
    global dx
    global dy

    if (dx == 0 and dy == 1):
        dx = 1
        dy = 0
    elif(dx == 1 and dy == 0):
        dx = 0
        dy = -1
    elif (dx == 0 and dy == -1):
        dx = -1
        dy = 0
    elif (dx == -1 and dy == 0):
        dx = 0
        dy = 1


user_n = int(input("Введите положительное целое число: "))

matrix_sc = get_matrix(user_n)
init_count = user_n ** 2
init_n = 1
dx = 0
dy = 1
ix = 0
iy = 0

while init_n <= init_count:
    matrix_sc[ix][iy] = init_n


    if 0 > (ix + dx) or (ix + dx) == (user_n) or 0 > (iy + dy) or  (iy + dy) == (user_n):
        change_dir()
    if matrix_sc[ix + dx][iy + dy] != 0:
        change_dir()

    ix += dx
    iy += dy
    init_n += 1

for row in matrix_sc:
    for cel in row:
        print('{:4d}'.format(cel), end=" ")
    print("")
