"""
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
"""

file1 = open('ur1.txt');
u1 = file1.read();
file1.close();

u1 = u1[0: len(u1)-4]
u1List = u1.split(' + ')

file2 = open('ur2.txt');
u2 = file2.read();
file2.close();

u2 = u2[0: len(u2)-4]
u2List = u2.split(' + ')

def uDic(userList):
    uDic = {}
    for i in range(0, len(userList)):
        result = ""
        userKey = '0'
        for j in range(0, len(userList[i])):
            if not userList[i][j].isdigit():
                userKey = userList[i][j:]
                break;
            result = result + userList[i][j]
        if userKey != '0':
            if result=="":
                uDic[userKey] = int(1);
            else:
                uDic[userKey] = int(result);
        else:
            if result=="":
                uDic['0'] = 0;
            else:
                uDic['0'] = int(result);
    return uDic;
        
ur1 = uDic(u1List)
ur2 = uDic(u2List)

def UrMultiplication(userUr1, userUr2):
    result = ""

    if len(userUr2)>len(userUr1):
        userUr1, userUr2 = userUr2, userUr1

    for uKey in userUr1:
        if uKey in userUr2:
            if uKey != "0":
                result = result + str(userUr1[uKey]+userUr2[uKey])+uKey + " + "
            else:
                result = result + str(userUr1[uKey]+userUr2[uKey])
        else:
            if uKey != "0":
                result = result + str(userUr1[uKey])+uKey + " + "
            else:
                result = result + str(userUr1[uKey])
    result = result + " = 0"
    file3 = open("result.txt", 'w');
    file3.write(result);
    file3.close();


UrMultiplication(ur1, ur2)