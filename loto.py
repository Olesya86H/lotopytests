#!/usr/bin/env python
# coding: utf-8

# # This is a sample Jupyter Notebook
# 
# Below is an example of a code cell. 
# Put your cursor into the cell and press Shift+Enter to execute it and select the next one, or click !here goes the icon of the corresponding button in the gutter! button.
# To debug a cell, press Alt+Shift+Enter, or click !here goes the icon of the corresponding button in the gutter! button.
# 
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 
# To learn more about Jupyter Notebooks in PyCharm, see [help](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html).
# For an overview of PyCharm, go to Help -> Learn IDE features or refer to [our documentation](https://www.jetbrains.com/help/pycharm/getting-started.html).

# In[36]:


import random

class Card:
    def __init__(self):
        self.card = self.get_card()

    def get_card(self):
        card = []
        ranges = [(1, 18), (19, 37), (38, 56), (57, 75), (76, 90)]
        for low, high in ranges:
            column = random.sample(range(low, high + 1), 5)
            card.append(column) #добавили число на карточку
        return card

    def output_card(self):
        a = [] #массив с числами в строке - для вывода на экран с учетом свободных полей
        for row in range(3):
            spaces = random.sample(range(1,9), 4) #массив с позициями пропусков в карточке
            for col in range(5):
                value = self.card[col][row]
                a.append(value)
            #только вывод строки из карточки, как в ТЗ:
            str_ = ""
            j = 0
            i = 1
            while i <= 9 :
                if i in spaces:
                    str_ = str_ + "  "
                else:
                    str_ = str_ + str(a[j]) + " "
                    j += 1
                i += 1
            print(str_)
            a = []
        print()

class Loto:
    def __init__(self, players):
        self.players = [Card() for i in range(players)] #сделали по карточке на каждого игрока
        self.barrel_numbers = set() #обнуляем мн-во бочонков

    def barrel_number(self):
        while True:
            number = random.randint(1, 90)
            if number not in self.barrel_numbers:
                self.barrel_numbers.add(number)
                return number
        
    def check_winner(self, card):
        # Проверка элементов в строках
        for row in range(3):
            if all(item in self.barrel_numbers for item in [card.card[col][row] for col in range(5)]):
                return True
        # Проверка колонок
        for col in range(5):
            if all(item in self.barrel_numbers for item in card.card[col]):
                return True
        return False
        
    def start(self):
        for i, card in enumerate(self.players):
            print(f"Карточка игрока {i + 1}:")
            card.output_card()

        winner = None
        while not winner:
            number = self.barrel_number()
            print(f"Новый бочонок: {number}")
            for i, card in enumerate(self.players):
                if self.check_winner(card):
                    winner = i
                    break

        return winner + 1
        #print(f"Игрок {winner + 1} выиграл!")

if __name__ == "__main__":
    try:
        players_cnt = int(input("Введите кол-во игроков: "))
        if players_cnt == 1:
            print("Кол-во игроков не распознано, по умолчанию будет 2 игрока: Вы и комп")
            players_cnt = 2
    except:
        print("Кол-во игроков не распознано, по умолчанию будет 2 игрока: Вы и комп")
        players_cnt = 2
    loto = Loto(players = players_cnt)
    print(f"Игрок {loto.start()} выиграл!")


# In[23]:





# In[ ]:




