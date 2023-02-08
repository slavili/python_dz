'''
Самостоятельная практика №2
    Показать median_house_value где median_income < 2
    (Доп) Показать данные в первых 2 столбцах
    (Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000

'''
import pandas as pd

userData = pd.read_csv('california_housing_test.csv')
print(userData)
#Показать median_house_value где median_income < 2
print(userData.loc[userData['median_income'] < 2, ['median_house_value']])
#(Доп) Показать данные в первых 2 столбцах
print(userData[['longitude', 'latitude']])
#(Доп) Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(userData[(userData['housing_median_age'] < 20) & (userData['median_house_value'] > 70000)])