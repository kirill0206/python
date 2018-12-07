
__author__ = 'AKV'

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""


import random


class Card:

    @staticmethod
    def _generate_card():
        pass

    def __init__(self):
        self.card_numbers = Card._generate_card()

    # !при удалении удаляем иликак-то изменяем цифру?
    def remove_number_from_card(self, number):
        if number in self.card_numbers:
            self.card_numbers.remove(number)

    def print_card(self):
        pass

    def remove_keg(self, keg):

class Player:

    def __init__(self, name):
        self.name = name
        self.card = None

    def action(self, keg):
        act = input()
        if act.lower() == 'y':
            if keg in self.card:
                self.card.remove(keg)
                return None
            else:
                return "End"
        if act.lower() == 'n':
            if keg in self.card:
                return "End"



class Dialer:

    def __init__(self):
        self.keg_in_bag = list(range(1, 90))

    def get_keg(self):
        random.shuffle(self.keg_in_bag)
        keg = self.keg_in_bag.pop()
        print('Новый бочонок: {} (осталось {})'.format(keg, len(self.keg_in_bag)))
        return keg

    def get_keg_list(self):
        return self.keg

    def set_card(self):
        card = Card()
        return card

    @staticmethod
    def say(words):
        print(words)

class Game:

    def game_start(self):

        player = Player("Player")
        comp = Player("Computer")
        dialer = Dialer()
        player.card = dialer.set_card()
        comp.card = dialer.set_card()

        while player.is_loose or player.is_win or comp.is_win:
            keg = dialer.get_keg()
            player.card.print("Ваша карточка")
            comp.card.print("Карточка компьютера")
            dialer.say("Зачеркнуть цифру? (y/n)")
            player.action(keg)





