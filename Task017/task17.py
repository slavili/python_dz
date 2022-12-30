"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

n = int(input('Введите натуральное число: '));
delitel = 2;
while n > 1:
    if n%delitel==0:
        n = n/delitel;
        print(delitel, end = " ");
    else:
        delitel = delitel + 1;
    