name1 = "незнакомец"
name2 = "мистееер"

print("Hello, " + name1)
print("Чей сам будешь, " + name2)
print("С какой целью интересуешься, " + name1)
print("Зачем такой грубый, а, " + name2)

name = 10

print(name)

random_bool = True

print(random_bool)

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[4])

weekDays = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]

total_days = len(weekDays)
print(total_days)

#сокращение функции len
print(len(weekDays))

mondey = weekDays[0]
print(mondey)

thursday = weekDays[3]
print(thursday)
#сокращение за счёт того, что не прописана лишняя переменная, знак равенства не нужен, т.к. выводим только значение
print(weekDays[6])

def greet(name):
    print("Hello, " + name)


def sum(num1, num2):
    result = num1 + num2
    print(result)
    return result


def multy(x, y):
    return x * y


def sub(a, b):
    return a / b


def div(t, p):
    return t - p


def pls(f, v, w):
    return f * v / w


total_days = len(weekDays)
print(total_days)
#сокращение функции len
print(len(weekDays))
mondey = weekDays[0]
print(mondey)
thursday = weekDays[3]
print(thursday)
#сокращение за счёт того, что не прописана лишняя переменная, знак равенства не нужен, т.к. выводим только значение
print(weekDays[6])

greet("Alex")
greet("Mark")

x = sum(10, 100)
print(x)

m = multy(200, 100)
print(m)

s = sub(256, 12)
print(s)

d = div(28, 7)
print(d)

p = pls(28, 7, 5)
print(p)

#Области видимости переменной

GlobalVar = 1

def print_global():
    print(GlobalVar)

def print_local():
    locale = 2
    print(locale)

print_global()
print_local()

#print(local) выдаст ошибку, т.к. local находится в функции print_local(), и кроме этой функции нигдк использоваться не может.

#СТЕК ВЫЗОВОВ

def funcA():
    print("Начали выполнять функцию А")
    funcB()
    print("Закончили выполнять функцию А")

def funcB():
    print("Начали выполнять функцию В")
    funcC()
    print("Закончили выполнять функцию В")

def funcC():
    print("Начали выполнять функцию C")
    funcD()
    print("Закончили выполнять функцию C")

def funcD():
    print("Начали выполнять функцию D")
    print("Закончили выполнять функцию D")

funcA()

def endless():
    print(endless)
    endless()

endless()