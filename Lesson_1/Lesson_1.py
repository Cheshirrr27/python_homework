name1 = "Константин"
name2 = "мистееер Кот" # значение (имя) пишется в кавычках

print("Hello, " + name1)
print("Как сам, " + name2)
print("С какой целью интересуешься, " + name1)
print("Зачем такой грубый, а, " + name2)

name = 10 # числовое значение пишется числом БЕЗ дополнительных символов

print(name)

random_bool = True # True и False пишутся без дополнительных символов, обязательно с большой буквы

print(random_bool)

# СПИСКИ

numbers = [10, 20, 30, 40, 50] # список пишется в КВАДРАТНЫХ скобках, через ЗАПЯТУЮ. Значение (имя), пишется в кавычках, внутри квадратных скобок.

print(numbers[0])
print(numbers[-1])

weekDays = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]


print(len(weekDays)) #сокращение функции len

mondey = weekDays[0] # индекс указывается в квадратных скобках
print(mondey)

thursday = weekDays[3]
print(thursday)
print(weekDays[6]) #сокращение за счёт того, что не прописана лишняя переменная, знак равенства не нужен, т.к. выводим только значение

# ФУНКЦИИ

def greet(name): # 
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
print ('Hello, World')