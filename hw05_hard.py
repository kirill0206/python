
#HARD

# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os

BASE_DIR = r"C:\Users\User1\Desktop\Kirill\Test5"

files = os.listdir(BASE_DIR)

extension_dirs = set([file for file in files
                      if os.path.isdir(os.path.join(BASE_DIR, file))])

for ext in extension_dirs:
    for file in os.listdir(os.path.join(BASE_DIR, ext)):
        os.rename(os.path.join(BASE_DIR, ext, file)
        os.path.join(BASE_DIR, file))
        os.rmdir(os.path.join(BASE_DIR, ext))