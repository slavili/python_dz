import model as m

#Вывод на экран всех абонентов с телефонами, либо точечно по Фамилии
def printAllAbonents(lastName = 0):
    listPhones = m.getData("phones.db");
    listAbonents = m.getData("abonents.db");
    rString = ""
    if lastName == 0:
        for ph in listPhones:
            for ab in listAbonents:
                if ph[0] == ab[0]:
                    rString += f"{ab[0].strip()} {ab[1].strip()} {ab[2].strip()} Тел.:  {ph[1].strip()}\n"
    else:
        for ph in listPhones:
            for ab in listAbonents:
                if ph[0] == ab[0] and lastName == ab[1].strip():
                    rString += f"{ab[0].strip()} {ab[1].strip()} {ab[2].strip()} Тел.:  {ph[1].strip()}\n"
    if rString == "":
        return "Абонент с такой фамилией отсуствует"
    return rString

#Вывод на экран всех абонентов с телефонами, либо точечно по Фамилии
def searchAbonentsById(idAbonent):
    listPhones = m.getData("phones.db");
    listAbonents = m.getData("abonents.db");
    rString = ""
    for ph in listPhones:
        for ab in listAbonents:
            if ph[0] == ab[0] and int(idAbonent) == int(ab[0].strip()):
                rString += f"{ab[0].strip()} {ab[1].strip()} {ab[2].strip()} Тел.:  {ph[1].strip()}\n"
    if rString == "":
        return f'"Абонент с id = {idAbonent} отсуствует"'
    return rString

#Вывод на экран абонентов без привяки к телефонам
def printAbonentsWithoutPhones():
    listAbonents = m.getData("abonents.db");
    rString = ""
    for ab in listAbonents:
        rString += f"{ab[0].strip()} {ab[1].strip()} {ab[2].strip()}\n"
    return rString

#Добавление нового абонена в формате CSV
def addAbonent(lastName, name):
    dataBase = "abonents.db"
    rString=f"{getMaxIdFromAbonents()+1},{lastName},{name}"
    m.setItem(dataBase, rString);

#Добавление телефона абонента
def addPhone(idAbonent, phoneNumber):
    rString = f"{idAbonent},{phoneNumber}"
    m.setItem("phones.db", rString)


#Получение максимального  ID из таблицы абонентов
def getMaxIdFromAbonents():
    listAbonents = m.getData("abonents.db");
    tempList = list(map(lambda x: int(x), [i[0] for i in listAbonents]))
    return max(tempList)

#Перед добавлением в таблицу Телефоны idАбонента и его телефон проверяется существует ли такой id в таблице Абонентов
def VerificationIdAbonent(idAbonent):
    listAbonents = m.getData("abonents.db");
    tempList = list(map(lambda x: int(x),[i[0] for i in listAbonents]))
    flag = False
    if idAbonent in tempList: flag = True
    return flag