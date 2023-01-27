'''
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
Идентификатор пользователя начинать с 1 и так далее.
Связь абонентов с телефонами: один ко многим.
'''
import controller as c

uVar=0
while uVar!=5:
    uVar = c.show_menu();
    print(f"Выбран пункт: {uVar}")
    if uVar == 0:
        print(c.printAllAbonents())
    elif uVar == 1:
        c.addAbonent()
    elif uVar == 2:
        c.addPhone()
    elif uVar == 3:
        c.intoXML()
    elif uVar == 4:
        c.intoJSON()