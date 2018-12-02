__author__ = 'Aristarkhov Kirill Viktorovich'

#HARD
#Задание-1
#Написать консольное меню вида:
#1. Добавить
#2. Удалить
#3. Распечатать
#4. Посчитать
#5. Выйти
#Надо чтобы
#а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
#б) Каждое действие (добавить, удалить и тд) должно быть функцией
#в) У пользователя надо спросить номер команды
#г) Программа не должна завершаться пока не введется команда Выйти
#д) Проверять на ввод ошибочных данных, там где они могут появиться


def print_menu(lst_menu):
    for idx, val in enumerate(lst_menu):
        print(str(idx + 1) + ".  " + val)
    print("=" * 80)


def add_menu(lst_menu):
    while True:
        number = input("Введите номер пункта меню который надо добавить: ")
        if check_num(number, lst_menu):
             break
    number = int(number) - 1
    name = input("Введите название пункта меню: ")
    return lst_menu[:number] + [name] + lst_menu[number:]

def del_menu(lst_menu):
    while True:
        number  = input("Введите номер пункта меню который надо удалить: ")
        if check_num(number, lst_menu):
             break
        else:
            print("Введен неправильный номер меню")

    number = int(number)
    return lst_menu[:number-1] + lst_menu[number:]


def check_num(num, lst_menu) -> bool:
    if num.isdigit():
         if int(num) > 0:
             if int(num) <= len(lst_menu):
                return True
    return False


def change_menu(lst_menu):
    print("Вы вырбрали поменять пункты местами.")
    while True:
        number1  = input("Введите номер 1 пункта: ")
        if check_num(number1, lst_menu):
             break
        else:
            print("Введен неправильный номер меню")
    number1 = int(number1) - 1

    while True:
        number2  = input("Введите номер 2 пункта: ")
        if check_num(number2, lst_menu):
            if number2 != number1:
                 break
            else:
                print("Необходимо выбрать другой номер, не равный номеру первого пункта!")
        else:
            print("Введен неправильный номер меню")
    number2 = int(number2) - 1

    lst_menu[number1], lst_menu[number2] = lst_menu[number2], lst_menu[number1]
    return lst_menu

menu = ["Добавить", "Удалить", "Распечатать", "Посчитать", "Выйти"]
actions = ["Напечатать меню", "Добавить пункт меню", "Удалить пункт меню", "Поменять пунты местами", "Выйти"]

while True:
    print("Программа по корректировке меню")

    print ("Выберите действие: ")
    print_menu(actions)

    check = False
    while not check:
        user_answer = input("Ваш выбор: ")
        check = check_num(user_answer, actions)
        if not check:
            print("Введено некорректное значение")

    user_answer = int(user_answer)


    if user_answer == 1:
        print_menu(menu)

    elif user_answer == 2:
        menu = add_menu(menu)

    elif user_answer == 3:
        menu = del_menu(menu)

    elif user_answer == 4:
        menu = change_menu(menu)

    elif user_answer == 5:   # len(actions) проверка что не выбрана команда "Выйти"
        break
