'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

sourceString = '''Еще дуют абвхолодные ветры
И нанабвосят утренни морозы,
Только что наабв проталинах весенних
Покабвазались ранабвние цветочки'''
searchString = 'абв';
print(sourceString);
print('----------Разделитель строк-------------');
sourceString=sourceString.replace(searchString,'');
print(sourceString);