#Извлечь таблицу всех сотрудников
def getData(dataBase):
    resultList = []
    with open(dataBase, "r", encoding='utf-8') as file_open:
        resultList = list(map(lambda x: x.split(','), (i for i in file_open.readlines())))        
    return resultList

#Получить название должности по идентификатору
def getItem(dataBase, item):
    resultList = []
    with open(dataBase, "r", encoding='utf-8') as file_open:
        resultList = list(map(lambda x: x.split(','), (i for i in file_open.readlines())))
    for tempItem in resultList:
        if tempItem[0] == item:
            return tempItem[1]
    return 'Неизвестная должность'

#Добавить строку в конец файла
def setData(dataBase, rString):
    with open(dataBase, "a", encoding='utf-8') as file_open:
        file_open.write(rString);

#Переписать таблицу сотрудников
def replaceDatabase(dataBase, List):
    f = open(dataBase, "r+")   
    f.seek(0) 
    f.truncate()
    f.close()
    rString = ""
    for i in List:
        rString+=",".join(i)
    setData(dataBase, rString)