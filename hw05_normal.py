
__author__ = 'Aristarkhov Kirill Viktorovich'

import os
import shutil
import hw05_easy

#NORMAL

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def print_menu(menu_name):
    for i,k in enumerate(menu_name):
        print(f"{i+1}. {k}")


def follow_to_path(path_name):
    global directory
    os.path.join(path_name)
    directory = os.path.getcwd()


def get_folder_name():
    return input("Введите имя папки: ")


def create_folder():
    name = get_folder_name()
    hw05_easy.create_folder(name, 1, directory)
# Вернуть статус выполнения команды


def remove_folder():
    name = get_folder_name()
    if os.path.exists(f"{directory}{name}"):
        hw05_easy.remove_folder(name, 1, directory)
# Вернуть статус выполнения команды


def get_command(max) -> int:

    while True:
        command = int(input("Ваш выбор:"))
        if command is not None and 0 < command <= max:
            break
        else:
            print("Неправильно введен номер команды!")

    return command


def exit_programm():
    exit(0)


directory = ""
menu = {
    "Перейти в папку": follow_to_path,
    "Просмотр папки": hw05_easy.ls_dir(),
    "Удалить папку": hw05_easy.remove_folder(),  #???? как удалят
    "Создать папку": create_folder(),  #???? надо ввести имя создаваемой папки
    "Выйти": exit_programm
}

while True:
    print_menu(menu)
    command_num = get_command(len(menu))
    menu[list(menu.keys())[command_num - 1]]()