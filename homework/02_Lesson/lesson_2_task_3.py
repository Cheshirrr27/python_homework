import math

def square(side):
    return math.ceil(side ** 2)

num_side = int(input("Введите длинну одной стороны: "))
print(f"Площадь квадрата = {square(num_side)}")