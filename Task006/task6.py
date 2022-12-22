"""
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    Пример:
- 6782 -> 23
- 0,56 -> 11
"""

def SummOfDigits(userNumber):
    result: int = 0;
    
    tempList = userNumber.split('.');
    tempValue = int(tempList[0]);

    if(len(tempList) > 1):
        tempValue = int(tempList[0] + tempList[1]);

    while(tempValue > 0):
        result+=tempValue%10;
        tempValue = tempValue//10

    return result;

print('Дробное число нужно вводить через точку');
userNumber = input('Введите число: ');

print(f'Сумма цифр {userNumber} = {SummOfDigits(userNumber)}');