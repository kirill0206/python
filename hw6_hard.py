
__author__ = 'Aristarkhov Kirill Viktorovich'


import time

#HARD

# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка

# Чем логичнее код тем лучше

class TrafficLight:
    light_green = bool
    light_yellow = bool
    light_red = bool

    def __init__(self):
        self.light_green = False
        self.light_yellow = False
        self.light_red = False

    def get_status(self):
        return f"({self.light_green},{self.light_yellow}, {self.light_red})"

    def set_green_on(self):
        if not self.light_green:
            if self.light_red:
                self.set_lightning_yellow()
                self.light_yellow = False
            if self.light_yellow:
                self.set_lightning_yellow()
                self.light_yellow = False
            self.light_green = True

    def set_red_on(self):
        if not self.light_red:
            if self.light_green:
                self.light_green = False
            if self.light_yellow:
                time.sleep(2.0)
                self.light_yellow = False
            self.light_green = True

    def set_ligthning(self, color):
        self.{color} = True
        time.sleep(0.5)
        self.light_yellow = False
        time.sleep(0.5)
        self.light_yellow = True
        time.sleep(0.5)
        self.light_yellow = False
        time.sleep(0.5)
        self.light_yellow = True
        time.sleep(0.5)


    def set_lightning_yellow(self):
        self.light_yellow = True
        time.sleep(0.5)
        self.light_yellow = False
        time.sleep(0.5)
        self.light_yellow = True
        time.sleep(0.5)
        self.light_yellow = False
        time.sleep(0.5)
        self.light_yellow = True
        time.sleep(0.5)


# Задание-2: не обязательно
#
# Написать консольную РПГ игру...
# Пример:

# <Характеристики персонажа>   <Характеристики врага>
# (HP, MP, Power, Defense)
#
# <Выбор действий>
# (Атаковать, Лечиться, .....)

class Unit:

    def __init__(self, level):
        self.level = level

    def increase_level(self):
        self.level += 1

class War(Unit):

    def __init__(self, level = 1, hp = 200, atack = 25):
        super.__init__(level)
        self.hp = hp
        self.atack = atack

    def get_attack(self):
        self.atack = 25 + self.level * 3
        return self.atack

