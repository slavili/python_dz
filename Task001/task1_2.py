"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""

def funcDayOfWeeks(numberOfDay, userList):
    tempResult = None
    if numberOfDay >=1 and numberOfDay <=5:
        tempResult = f'{userList[numberOfDay - 1]} является рабочим днём.'
    elif numberOfDay == 6 or numberOfDay == 7:
        tempResult = f'{userList[numberOfDay - 1]}  - выходной день!!!'
    else:
        tempResult = f'Дня недели под номером {numberOfDay} не существует.'
    return tempResult

dayOfWeek = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']  

print('Является ли введённый день недели выходным?')
userDay = int(input('Введите номер дня недели от 1 до 7: '))

print(funcDayOfWeeks(userDay, dayOfWeek));