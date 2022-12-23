"""
    Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.(если получаются длинные числа после запятой, это нормально и особенность данного языка программирования. ваш ответ может не совпадать с примером(может получитя 0,20))

    Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

"""

import math
import random

#CreateUserList - функция наполнения списка случайными целочисленными элементами
def CreateUserList(n = 10,):
    tempList = []
    for i in range(n):
        tempList.append(round(random.paretovariate(1), 5));
    return tempList;

#DifferenceMaxMin - выдаёт словарь со значениями: максимальное дробное, минимально дробное, разность между максимальным дробным и минимальным дробным
def DifferenceMaxMin(userList):
    tempList = [];

    for i in userList:
        tempList.append(float("0."+str(i).split('.')[1]))
    
    maxValue = tempList[0];
    minValue = tempList[0];

    for i in range(1, len(tempList)):
        if tempList[i]> maxValue:
            maxValue =tempList[i]
        elif  tempList[i] < minValue:
            minValue = tempList[i]
    
    return {'maxValue':maxValue, 'minValue':minValue, 'difference':(maxValue-minValue)}

uL = CreateUserList()
print('Оригинальнй список');
print(uL)
dif = DifferenceMaxMin(uL)
print('Максимальная дробная часть {}'.format(dif['maxValue']));
print('Минимальная дробная часть {}'.format(dif['minValue']));
print('Разность м/у максимальной и минимальной {}'.format(dif['difference']));
