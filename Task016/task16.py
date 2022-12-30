"""
    Вычислить число c заданной точностью d
    Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

def Pi(d = 0.001):
    i = 0;
    first = (-1)**i/(2*i+1)
    second =(-1)**i/(2*i+1)+ ((-1)**(i+1))/(2*(i+1)+1)
    while abs(first-second) >= d:
        i = i+1;
        first =first+ (-1)**i/(2*i+1)
        second =second + ((-1)**(i+1))/(2*(i+1)+1)   
    return 4*first;
print(Pi(0.001))