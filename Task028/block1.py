'''
Самостоятельная практика №1
    Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
    Посмотреть сколько в нем строк и столбцов
    (Доп) Определить какой тип данных имеют столбцы
    (Доп) Проверить есть ли в файле пустые значения
'''
import pandas as pd
import matplotlib.pyplot as plt

#Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
userData = pd.read_csv('california_housing_test.csv')
print(userData)
#Посмотреть сколько в нем строк и столбцов
print(userData.shape)
#(Доп) Определить какой тип данных имеют столбцы
print(userData.dtypes)
#(Доп) Проверить есть ли в файле пустые значения
print(userData.isnull().sum())