import os


def getData(dataBase = "abonents.db"):
    resultList = []
    with open(dataBase, "r", encoding='utf-8') as file_open:
        resultList = list(map(lambda x: x.split(','), (i for i in file_open.readlines())))        
    return resultList

#Запись строки в любой справочник(абоненты, телефоны)
def setItem(dataBase, rString):
    fileSize = os.path.getsize(dataBase)#Нужно для переноса строки
    with open(dataBase,"a", encoding='utf-8') as openFile:
        if fileSize > 0:
            openFile.write(f"\n{rString}");
        else:
            openFile.write(rString);