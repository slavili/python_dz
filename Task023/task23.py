'''
Создайте программу для игры в ""Крестики-нолики"".

Первый ход за игроком(крестик). Необходимо вводить номер элемента двумерного массива,
например центральный элемент вводим: 1 1 - обязательно через пробел
Бот не умный, бот случайный.
'''
import random

TestList = [[1,1,1],[1,1,1],[1,1,1]]

#print(TestList)

#функция заполнения полей ноликами о имени компьютера
def addBotItem():
    tempList = [];
    x = len(TestList)
    y = len(TestList[0])
    for i in range(x):
        for j in range(y):#собираем координаты незанятых полей в отдельный список
            if TestList[i][j] == 1:
                tempList.append([i,j]);
    if len(tempList)>0:
        #print(tempList)
        uRnd = random.randint(0, len(tempList)-1)
        #print(uRnd)
        TestList[tempList[uRnd][0]][tempList[uRnd][1]] = '0'


#Функция проверки победилея
def Proverka(userVar):
    x = len(TestList)
    y = len(TestList[0])
    result = 0
    #проверка по горизонтали
    for i in range(x):
        for j in range(y):
            if userVar == TestList[i][j]:
                result = result + 1
        if result == 3:
            return f'{userVar}'
        else:
            result = 0;
    #проверка по вертикали
    for i in range(x):
        for j in range(y):
            if userVar == TestList[j][i]:
                result = result + 1
        if result == 3:
            return f'{userVar}'
        else:
            result = 0;
    #проверка по главной диагонали
    for i in range(x):
        if userVar == TestList[i][i]:
            result = result + 1
    if result == 3:
        return f'{userVar}'
    else:
        result = 0; 
    #проверка по не главной диагонали
    for i in range(x):
        if userVar == TestList[x-1-i][i]:
            result = result + 1
    if result == 3:        
        return f'{userVar}'
    else:
        result = 0;
    return ''




while True:
    userStepList = []

    for i in TestList:
        print(*i)


    print('Ваш ход');
    userStepList = list(map(int, input().split()));

    #в данном if ставим крестик как пользователь
    #если крестик в данном поле можно установить, то он устанавливается
    #затем сразу устанавливается нолик
    if TestList[userStepList[0]][userStepList[1]] == 1:
        TestList[userStepList[0]][userStepList[1]] = 'x';
        addBotItem();

    if Proverka('x') == 'x':
        print('Победил игрок')
        for i in TestList:
            print(*i)
        break;
    elif Proverka('0') == '0':
        print('Победил компьютер')
        for i in TestList:
            print(*i)
        break;