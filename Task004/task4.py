"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""
# CheckDiapason - функция, проверят номер переданной четверти 
# и выдаёт диапазон координат точек в это четверти
def CheckDiapason(numberOfQuarter):    
    if numberOfQuarter == 1:
        tempValue = 'X∈(0;+∞), Y∈(0;+∞)'
    elif numberOfQuarter == 2:
        tempValue = 'X∈(-∞;0), Y∈(0;+∞)'
    elif numberOfQuarter == 3:
        tempValue = 'X∈(-∞;0), Y∈(-∞;0)'
    elif numberOfQuarter == 4:
        tempValue = 'X∈(0;+∞), Y∈(-∞;0)'
    else:
        tempValue = -1 # в функцию передана несуществующая четверть
    return tempValue

print('Необходимо ввести номер четверти от 1 до 4.')
userQuarter = int(input('Введите номер четверти: '))

print(CheckDiapason(userQuarter))