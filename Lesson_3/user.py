class User:

     age = 0;                                        # (ЭТО ПОЛЕ) дефолтное значение для всех экземпляров (для каждого участника класса)

     def __init__(self, name):                       # (ЭТО КОНСТРУКТОР)
         print ('я создался ')
         self.username = name                       # (ЭТО ПОЛЕ) в конструкторе создаём поле username через self "self.username"
        

     def sayName(self):                              # (ЭТО МЕТОД) "Скажи имя", но область видимости переменной не позволяет увидеть name, поэтому в конструкторе (32 строчка)
          print ('My name is - ', self.username)

     def sayAge(self):                               # (ЭТО МЕТОД) "Скажи возраст"
         print(self.age)

     def setAge(self, newAge):                       # (ЭТО МЕТОД) смена возраста
         self.age = newAge

     def addCard(self, card):                        # (ЭТО МЕТОД) добавления карты
         self.card = card

     def getCard(self):                              # (ЭТО МЕТОД) 
         return self.card