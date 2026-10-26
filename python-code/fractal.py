import math
import color as c
from decimal import Decimal

def distance(a):
    return math.sqrt(pow(a[0],2)+pow(a[1],2))

def square(a,c):
    
    return [Decimal(pow(a[0],2))-Decimal(pow(a[1],2))+Decimal(c[0]),Decimal(2)*Decimal(a[0])*Decimal(a[1])]

def fractal(z, c):
    if z == 1:
        return c
    else:   
        return square(fractal(z-1,c),c)

m=""

size = 100

for i in range(4*size):
    for j  in range(4*size):
        p=[j/size-2.5,i/size-2]
        p = fractal(10,p)
        if distance(p) <= 2.0:
            m = m+"O"
        else:
            m = m+" "
    m = m+"\n"

open("fractal.txt","w").write(m)