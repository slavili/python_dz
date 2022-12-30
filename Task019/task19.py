"""
    Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
    Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random

def Uravnenie(userFile, k = 2, k_rnd = 100):
    result = ""
    while k>=0:
        if k > 1 :
            rnd = random.randint(0,100)
            if rnd > 0:
                if rnd > 1:
                    if result!="":
                        result = result +" + "+ str(rnd)+"x^"+str(k)
                    else:
                        result =  str(rnd)+"x^"+str(k)
                else:
                    if result !="":
                        result = result + " + " + "x^"+str(k)
                    else:
                        result = result + "x^"+str(k)
        elif k == 1:
            rnd = random.randint(0,100)
            if rnd > 0 and result!="":
                if rnd == 1:
                    result = result + " + " + "x"
                else:
                    result = result + " + " + str(rnd)+"x"
            elif rnd > 0 and result=="":
                if rnd == 1:
                    result = "x"
                else:
                    result = str(rnd)+"x"
        else:
            rnd = random.randint(0,100)
            if rnd > 0 and result!="":
                result = result + " + " + str(rnd)
        k = k - 1

    if result!="":
        result = result + " = 0"
        data = open(userFile,'w');
        data.write(result);
        data.close();



Uravnenie('task19.txt', 4, 100);