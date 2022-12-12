"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
from math import sqrt
#DistanceBetweenPoints - функция рассчёта расстояние между точками в двухметром пространстве
def DistanceBetweenPoints(A = [3,6], B = [2,1]):
    distance = sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
    return distance

pointA = []
pointB = []
print('Необходимо рассчитать расстояние между точками A и B по их координатам.')

xA = int(input('Введите координату x точки A: '))
pointA.insert(0, xA)
yA = int(input('Введите координату y точки A: '))
pointA.insert(1, yA)

xB = int(input('Введите координату x точки B: '))
pointB.insert(0, xB)
yB = int(input('Введите координату y точки B: '))
pointB.insert(1, yB)

print(f'Расстояние между точками A({pointA[0]},{pointA[1]}) и B({pointB[0]},{pointB[1]}) равно {DistanceBetweenPoints(pointA, pointB)}')