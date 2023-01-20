"""
Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
"""
'''
def UserFunction(n):
    tempValue: float = 0.0;

    tempValue = round((1 + 1/n)**n, 2);

    return tempValue;


userList = [];
userNumber = int(input('Введите целое число: '));

for i in range(1, userNumber+1):
    userList.append(UserFunction(i));

print(userList);
print(sum(userList));
'''

userNumber = int(input('Введите целое число: '));

userList = list(map(lambda n: round((1 + 1/n)**n, 2), [n for n in range(1, userNumber+1)]));

print(userList);
print(sum(userList));