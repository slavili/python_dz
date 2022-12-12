"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
Пример:
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""
# QuarterСheck - функция проверки номер четверти. 
# Если хотя бы один из переданных параметров равен нулю, то функция возвращает -1
def QuarterСheck(x, y):    
    if x > 0 and y > 0:
        tempValue = 1
    elif x < 0 and y > 0:
        tempValue = 2
    elif x < 0 and y < 0:
        tempValue = 3
    elif x > 0 and y < 0:
        tempValue = 4
    else:
        tempValue = -1 # если введён неверный формат данных
    return tempValue


x = int(input('Введите x: '))
y = int(input('Введите y: '))

print(f'Номер четверти: {QuarterСheck(x, y)}')