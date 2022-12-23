"""
    Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
#Fibonachi - вычисление чисел Фибоначчи с помощью хвостовой рекурсии
def Fibonachi(k = 8, first = -21, second = 13):
        if k <= 1:
            return first;
        return Fibonachi(k - 1, second, first+second)

userList = []

for i in range(1, 18):
    userList.append(Fibonachi(i))

print(userList);