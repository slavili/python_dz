"""
    Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""
import math
import random

#CreateUserList - функция наполнения списка случайными целочисленными элементами
def CreateUserList(n = 10, min = 1, max = 20):
    tempList = []
    for i in range(n):
        tempList.append(random.randint(min, max));
    return tempList;
    
#MultiplicationItemsOfList - функция премножения элементов списка 1*n, 2*(n-1) и т.д.
def MultiplicationItemsOfList(userList):
    tempList = []
    lenOfList = len(userList)
    numberOfCycles = math.ceil(lenOfList/2)
    for i in range(0, numberOfCycles):
        tempList.append(userList[i]*userList[lenOfList - i - 1])
    return tempList;


userList = CreateUserList(11)
#userList = [2, 3, 5, 6]
#userList = [2, 3, 4, 5, 6]

print(userList)
print(MultiplicationItemsOfList(userList))