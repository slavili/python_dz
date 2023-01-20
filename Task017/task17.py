"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""
'''
n = int(input('Введите натуральное число: '));
delitel = 2;
while n > 1:
    if n%delitel==0:
        n = n/delitel;
        print(delitel, end = " ");
    else:
        delitel = delitel + 1;
'''
def PrimeFactors(n):
    tempList = []
    delitel = 2;
    while n > 1:
        if n%delitel==0:
            n = n/delitel;
            tempList.append(delitel)
        else:
            delitel = delitel + 1;
    return tempList;

resultList = [(n, PrimeFactors(n)) for n in range(4, 30)]

print(resultList)