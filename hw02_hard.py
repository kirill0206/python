__author__ = 'Aristarkhov Kirill Viktorovich'

#Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
#1. Сколько слов в тексте?
#2. Сколько букв английского алфавита в тексте?

userStr = input("Введите текст: ")
specSymbol = (",.?!:()/;")
for symbol in specSymbol:
    userStr = userStr.replace(symbol, " ")

userList = userStr.split()
print("В тексте " + str(len(userList)) + " слов")

print(userStr)
engAlpha = ("abcdefghijklmnopqrstuvwxyz")
engChar = set()
for char in userStr:
    if char in engAlpha:
        engChar.add(char)
print(str(len(engChar)) + " букв латинского алфавита")

#Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра
"""
userAStr = (input("Введите текст: ")).lower()
userASet = set(userAStr.split())

userBStr = (input("Введите текст: ")).lower()
userBSet = set(userBStr.split())

resultWords = [word for word in userASet if word in userBSet]
"""
