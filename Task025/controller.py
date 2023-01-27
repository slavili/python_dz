import model as m

def printAllAbonents():
    listPhones = m.getData("phones.db");
    listAbonents = m.getData("abonents.db");
    rString = ""
    for ph in listPhones:
        for ab in listAbonents:
            if ph[0] == ab[0]:
                rString += f"{ab[0].strip()} {ab[1].strip()} {ab[2].strip()} {ph[0].strip()} {ph[1].strip()}\n"
    return rString

def intoXML():
    f = open("listPhones.xml", "w+")   
    f.seek(0) 
    f.truncate()
    f.close()
    resultString="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    resultString+="<root>\n"
    listPhones = m.getData("phones.db");
    listAbonents = m.getData("abonents.db");   
    for ab in listAbonents:
        resultString+=f"<abonent id=\"{ab[0].strip()}\" lastName=\"{ab[1].strip()}\" name=\"{ab[2].strip()}\">\n"
        for ph in listPhones:
            if ph[0] == ab[0]:
                resultString+=f"\t<phone>{ph[1].strip()}</phone>\n"
        resultString+="</abonent>\n"
    resultString+="</root>"
    m.setItem("listPhones.xml", resultString);

def intoJSON():
    f = open("listPhones.json", "w+")   
    f.seek(0) 
    f.truncate()
    f.close()
    resultString=""
    listPhones = m.getData("phones.db");
    listAbonents = m.getData("abonents.db");   
    for ab in listAbonents:
        resultString+="{\n"
        resultString+=f"\"id\":\"{ab[0].strip()}\",\n\"lastName\":\"{ab[1].strip()}\",\n\"firstName\":\"{ab[2].strip()}\",\n\"phones\":"
        resultString+="{\n"
        counter = 1
        for ph in listPhones:
            if ph[0] == ab[0]:
                if counter > 1:
                    resultString+=",\n"
                resultString+=f"\t\"phone{counter}\":\"{ph[1].strip()}\""
                
                counter+=1
        resultString+="\n}"  
        resultString+="\n}\n"    
    m.setItem("listPhones.json", resultString);


#Добавление нового абонена в формате CSV
def addAbonent(dataBase = "abonents.db"):
    rString = ""
    id = input("Введите идентификатор нового абонента: ");
    lastName = input("Введите фамилию нового абонента: ");
    name = input("Введите имя нового абонента: ");
    rString=f"{id},{lastName},{name}"
    m.setItem(dataBase, rString);

#Добавление телефона абонента
def addPhone(dataBase = "abonents.db"):
    tempList = m.getData(dataBase)
    rString = "Абоненты:\n"
    for i in tempList:
        rString+=f"{i[0]} {i[1]} {i[2]}"
    print(rString)
    idAbonent = input("Введите ID абонента: ")
    phoneNumber = input("Введите номер телефона абонента: ")
    rString = f"{idAbonent},{phoneNumber}"
    m.setItem("phones.db", rString)




def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("0. Весь список сотрудников с телефонами")
    print("1. Добавить абонента")
    print("2. Добавить телефон абонента")
    print("3. Экспортировать данные в формате XML")
    print("4. Экспортировать данные в формате JSON")
    print("5. Закончить работу")
    return int(input("Введите номер необходимого действия: "))