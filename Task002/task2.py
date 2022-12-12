"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.
"""

def TruthTest(x, y, z):
    tempValue = False
    if not(x or y or z) == (not x or not y or not z):
       tempValue = True
    return tempValue

x = 0
y = -10
z = 'Юрий Гагарин'

print(TruthTest(x, y, z))