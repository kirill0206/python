__author__ = 'Aristarkhov Kirill Viktorovich'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits) -> float:


    num_1 = number * (10 ** ndigits)
    if ((num_1 % 10) >= 5):
        num_1 += 1
    return (int(num_1) / (10 ** ndigits))


print(my_round(2.1234567, 5))

print(my_round(2.1999967, 5))

print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def sum_str_num(str_num) -> int:
    sum_cip = 0
    for cipher in str_num:
        sum_cip += int(cipher)
    return sum_cip


def lucky_ticket(ticket_number) -> bool:
    str_ticket = str(ticket_number)
    half_len_str = int(len(str_ticket) / 2)
    return sum_str_num(str_ticket[0:half_len_str]) == sum_str_num(str_ticket[-half_len_str:])


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

