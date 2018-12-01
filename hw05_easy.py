
__author__ = 'Aristarkhov Kirill Viktorovich'

import os
import shutil


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_folder(name, count, path_to_dir=os.getcwd()):
    os.path.join(path_to_dir)
    for i in range(1, count + 1):
        if not os.path.exists(f"{name}_{i}"):
            os.mkdir(f"{name}_{i}")


def remove_folder(name, count, path_to_dir=os.getcwd()):
    os.path.join(path_to_dir)
    for i in range(1, count + 1):
        if os.path.exists(f"{name}_{i}"):
            os.rmdir(f"{name}_{i}")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def ls_dir(path_to_dir=os.getcwd()):
    os.listdir(path_to_dir)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file():
    path_to_file = os.path.splitext(__file__)
    file_name = f"{path_to_file[0]}copy{path_to_file[1]}"

    shutil.copyfile(__file__, file_name)
