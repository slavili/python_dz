'''
Задача: Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
'''
import controller as c

uVar=0
while uVar!=9:
    uVar = c.show_menu();
    print(f"Выбран пункт: {uVar}");
    #c.PrintAllEmployees()
    if uVar == 0:
        print(c.PrintAllEmployees());
    elif uVar == 1:
        print(c.getEmployee(int(input("Введите номер сотрудника: "))));
    elif uVar == 2:
        print(c.getPosts());
        print(c.getEmpoyeeByPost(int(input("Введите номер должности: "))));
    elif uVar == 3:
        print(c.getEmpoyeeByWage(int(input("Введите ЗП: "))));
    elif uVar == 4:
        print(c.getPosts());
        print("Добавление сотрудника:")
        print(c.setNewEmployee());
    elif uVar == 5:
        print(c.PrintAllEmployees());
        print(c.deleteEmployee(input("Введите номер сотрудника, которого нужно удалить: ")))
    elif uVar == 6:
        print(c.PrintAllEmployees());
        print(c.updateEmployee(input("Введите номер сотрудника, данные которого нужно обновить: ")))
    elif uVar == 7:
        c.intoJson();
    elif uVar == 8:
        c.intoCSV();