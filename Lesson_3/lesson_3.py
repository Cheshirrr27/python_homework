# СОЗДАНИЕ КЛАССА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class User:                                    # класс - набор данных, обозначаемых полями, ОБЩИЕ ДАННЫЕ БЕЗ КОНКРЕТИКИ

#     def __init__(self):                        # функция конструктор 
#         print ('я создался ')


# user1 = User()                                 # создание экземпляра класса User (КОНКРЕТНЫЙ ЮЗЕР))).)
# user2 = User()
# user3 = User()

# !!!!!!!!!!!!!!!!!!!!РАСШИРЕННЫЙ ВАРИАНТ (+ИМЯ)

# class User:

#     def __init__(self, name):                  # ДОБАВЛЯЕМ ПОЛЕ "ИМЯ"
#         print ('я создался ')
#         print ('My name is - ', name)          # + name или через запятую - имеет значение для синтаксиса, если результат одинаковый?


# Gay = User('Gay')                              # название переменной не играет роли, кроме как добавляет больше удобства в работе
# Juliy = User('Juliy')
# Cesar = User('Cesar')

# ПОЛЯ И МЕТОДЫ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# class User:

#     age = 0;                                        # (ЭТО ПОЛЕ) дефолтное значение для всех экземпляров (для каждого участника класса)

#     def __init__(self, name):                       # (ЭТО КОНСТРУКТОР)
#          print ('я создался ')
#          self.username = name                       # (ЭТО ПОЛЕ) в конструкторе создаём поле username через self "self.username"
        

#     def sayName(self):                              # (ЭТО МЕТОД) "Скажи имя", но область видимости переменной не позволяет увидеть name, поэтому в конструкторе (32 строчка)
#          print ('My name is - ', self.username)

#     def sayAge(self):                               # (ЭТО МЕТОД) "Скажи возраст"
#          print(self.age)

#     def setAge(self, newAge):                       # (ЭТО МЕТОД) смена возраста
#          self.age = newAge


# Gay = User('Gay')                                    # создание экземпляра 
# Juliy = User('Juliy')
# Cesar = User('Cesar')

# Gay.sayName()                                        # вызов метода скажи имя
# Gay.sayAge()                                         # вызов метода скажи возраст
# Gay.setAge(27)                                       # вызов метода смены возраста
# Gay.sayAge()                                         # вызов метода скажи возраст после смены возраста

# ВЗАИМОДЕЙСТВИЕ КЛАССОВ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from user import User    # из файла user импортируй User
from card import Card

Gay = User('Gay')

Gay.sayName()
Gay.setAge(27)
Gay.sayAge()

card = Card('1234 5678 9012 3456', '04/39', 'Gay Juliy Cesar')

Gay.addCard(card)
Gay.getCard().pay(1000)