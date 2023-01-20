'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''


sourceString = '''fffaadeee34###444^&&&&
^^^^^^22((((()))))
llhrfwertwruttttttttttta'''


print(sourceString)
searchSymbol=sourceString[0];
j=0;
numbers=[]
symbols=[]

sourceString = sourceString + " "
for i in sourceString:
    if i!=searchSymbol:
        numbers.append(j);
        symbols.append(searchSymbol);
        searchSymbol = i
        j = 1
    else:
        j = j+1

result=list(zip(numbers, symbols))
#print(result);

print('=================Разделитель строк====================')
stringResult=""
for i in range(len(result)):
    stringResult+=result[i][1]*result[i][0]

print(stringResult)