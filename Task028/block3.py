'''
Самостоятельная практика №3
    Определить какое максимальное и минимальное значение median_house_value
    (Доп) Показать максимальное median_house_value, где median_income = 3.1250
    (Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
'''
import pandas as pd

userData = pd.read_csv('california_housing_test.csv')
#Определить какое максимальное и минимальное значение median_house_value
print(userData['median_house_value'].max())
print(userData['median_house_value'].min())
#(Доп) Показать максимальное median_house_value, где median_income = 3.1250
print(userData.loc[userData['median_income'] == 3.1250, ['median_house_value']].max())
#(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
print(userData.loc[userData['median_house_value'] == userData['median_house_value'].min(), ['population']].max())