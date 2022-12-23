"""
    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
    Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""

import random;
#CreateUserList - функция наполнения списка случайными целочисленными элементами
def CreateUserList(n = 10, min = 1, max = 20):
    tempList = []
    for i in range(n):
        tempList.append(random.randint(min, max));
    return tempList;

#SumElementsOfList - функция суммирования элементова на нечётных позициях. 
#Элемент на нулевой позиции также не включён в сумму.
def SumElementsOfList(userList):
    tempSum: int = 0;
    for i in range(0,len(userList)):
        if i!=0 and i%2!=0:
            tempSum+=userList[i]
    return tempSum

#uL = [2, 3, 5, 9, 3]; # образец

uL = CreateUserList(6)
print('Оригинальный список: ')
print(uL);
print('Сумма элементов на нечётных позициях, нулевая позиция также не включена:')
print(SumElementsOfList(uL));