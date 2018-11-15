__author__ = 'Aristarkhov Kirill Viktorovich'
import math
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

#Допустим нам дано число num
num = int(input())

# поиск через for
strnum = str(num)
max = 0
for digit in strnum:
    if (max < int(digit)):
        max = int(digit)
print("Максимальная цифра ", max)

#поиск через while
mun = num
max = 0
while (mun != 0):
    if (max < (mun % 10)):
        max = mun % 10
    mun //= 10
print("Максимальная цифра ", max)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# через арифметические действия
a = a + b
b = a - b
a = a - b

# через побитовые операции ( но мне кажется что из-за особенностей python есть варианты когда такой код может не сработать правильно)
a = a ^ b
b = a ^ b 
a = a ^ b

# через синтаксис кортежей
a,b = b,a

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Найдем корни квадратного уравнения вида ax² + bx + c = 0")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
diskr = b**2 - 4*a*c
if (diskr < 0):
    print("Корней нет!")
elif (diskr ==0):
    x = (0 - b) / (2 * a)
    print("Это уравнение имеет один корень: x = ", x)
else:
    x1 = (0 - b + math.sqrt(diskr)) / (2 * a)
    x2 = (0 - b - math.sqrt(diskr)) / (2 * a)
    print("Это уравнение имеет два корня: x1 = %.4f" %x1 + " x2 = %.4f" %x2)
    