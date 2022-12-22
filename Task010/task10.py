"""
Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
"""
#Алгоритм Фишера—Йетса или как я его понял

import random

n = 20;
tempValue: int = 0;
randValue: int = 0;
userList = [];

for i in range(1, n+1):
    userList.append(i);

print('Оригинальный список:');
print(userList);

i = 1
while i < len(userList):
    randValue = random.randint(0, i)
    tempValue = userList[i]
    userList[i] = userList[randValue]
    userList[randValue] = tempValue
    i+=1;

print('Перемешанный список:');
print(userList);