"""
    Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

def DigitToTwo(userNumber):
    tempValue: str = ''
    while userNumber > 0:
        tempValue = str(userNumber%2) + tempValue
        userNumber//=2
    return tempValue;

uD = int(input('Введите целое число: '));
print(DigitToTwo(uD));