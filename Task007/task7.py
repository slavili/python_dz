"""
    Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
#Вычисление факториала с помощью хвостовой рекурсии
def Factorials(n, result = 1):
    if(n<1):
        return result;
    return Factorials(n-1, n*result);

n = int(input('Введите целое число: '));

listFactorials = [];

for i in range(1, n+1):
    listFactorials.append(Factorials(i));

print(listFactorials);