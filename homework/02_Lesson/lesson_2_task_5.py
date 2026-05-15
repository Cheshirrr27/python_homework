def month_to_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Неверный номер месяца, используйте диапазон от 1 до 12 включительно"

month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
