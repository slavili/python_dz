import model as m

#Вывод на экран всех должностей с идентификаторами
def getPosts():
    tempString=""
    postList = m.getData("post.db");
    for postItem in postList:
        tempString+= f"{postItem[0].strip()} {postItem[1].strip()}\n"
    return tempString;


#Вывод на экран список всех сотрудников
def PrintAllEmployees(dataBase = "employees.db"):
    tempEmployees = m.getData(dataBase)
    resultString = ""
    for empList in tempEmployees:
        empPost = m.getItem("post.db",empList[3]);
        resultString+= f"{empList[0].strip()} {empList[1].strip()} {empList[2].strip()} {empPost.strip()} {empList[4].strip()} руб.\n"
    return resultString;
    
#Поиск сотрудника по идентификатору        
def getEmployee(userId):
    tempEmployees = m.getData("employees.db")
    for empList in tempEmployees:
        if int(empList[0]) == userId:
            empPost = m.getItem("post.db",empList[3]);
            return (f"{empList[0].strip()} {empList[1].strip()} {empList[2].strip()} {empPost.strip()} {empList[4].strip()} руб.")
    return "Такого сотрудника не существует"

#Поиск сотрудника по должности
def getEmpoyeeByPost(postId):
    tempString=""
    tempEmployees = m.getData("employees.db")
    for empList in tempEmployees:
        if int(empList[3]) == postId:
            empPost = m.getItem("post.db",empList[3]);
            tempString +=f"{empList[0].strip()} {empList[1].strip()} {empList[2].strip()} {empPost.strip()} {empList[4].strip()} руб.\n"
    return tempString;

#Поиск сотрудников по заработной плате
def getEmpoyeeByWage(wage):
    tempString=""
    tempEmployees = m.getData("employees.db")
    for empList in tempEmployees:
        if int(empList[4]) == wage:
            empPost = m.getItem("post.db",empList[3]);
            tempString +=f"{empList[0].strip()} {empList[1].strip()} {empList[2].strip()} {empPost.strip()} {empList[4].strip()} руб.\n"
    return tempString;


#Добавление нового сотрудника
def setNewEmployee(dataBase = "employees.db"):
    resultString=""
    empId = input("Введите ID: ");
    lastName = input("Введите фамилию: ");
    firstName = input("Введите имя: ");
    postId = input("Введите номер должности: ");
    wage = input("Введите ЗП: ");
    resultString = f"\n{empId.strip()},{lastName.strip()},{firstName.strip()},{postId.strip()},{wage.strip()}";
    m.setData(dataBase, resultString)

#Удаление сотрудника по его номеру
def deleteEmployee(userId, dataBase = "employees.db"):
    tempList = m.getData(dataBase)
    for i in range(len(tempList)):
        if tempList[i][0] == userId:
            tempList.remove(tempList[i])
            break
    m.replaceDatabase(dataBase, tempList)    

#Обновление данных сотрудника по его номеру
def updateEmployee(userId, dataBase = "employees.db"):
    tempList = m.getData(dataBase)
    userId = int(userId)
    print("Меняем данные сотрудника:");
    for i in range(len(tempList)):
        if int(tempList[i][0]) == userId:
            post = m.getItem("post.db",tempList[i][3])
            print(f"Текущая фамилия: {tempList[i][1]}")
            tempList[i][1]=input("Введите новую фамилию: ")
            print(f"Текущее имя: {tempList[i][2]}")
            tempList[i][2]=input("Введите новое имя: ")
            print(f"Текущая должность: {post.strip()}")
            tempList[i][3]=input("Введите новую должность(цифра): ")
            print(f"Текущая ЗП: {tempList[i][4]}")
            tempList[i][4]=input("Введите новую ЗП: ")+"\n"
            break
    m.replaceDatabase(dataBase, tempList)  

#Конвертировать в формат JSON
def intoJson(dataBase = "employees.db"):
    f = open("employee.json", "w+")   
    f.seek(0) 
    f.truncate()
    f.close()
    resultString=""
    tempList = m.getData(dataBase)    
    for i in tempList:
        post = m.getItem("post.db",i[3])
        resultString+="{"
        resultString+=f"\"id\":\"{i[0]}\", \"lastName\":\"{i[1]}\", \"name\":\"{i[2]}\", \"post\":\"{post.strip()}\", \"wage\":\"{i[4].strip()}\""
        resultString+="}\n"
    m.setData("employee.json", resultString);

#Конвертирова в формат CSV
def intoCSV(dataBase = "employees.db"):
    f = open("employee.csv", "w+")   
    f.seek(0) 
    f.truncate()
    f.close()
    resultString=""
    tempList = m.getData(dataBase)    
    for i in tempList:
        post = m.getItem("post.db",i[3])
        resultString+=f"{i[0]},{i[1]},{i[2]},{post.strip()},{i[4].strip()}\n"
    m.setData("employee.csv", resultString);

def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("0. Весь список сотрудников")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
