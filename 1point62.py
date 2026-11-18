#unfinished
from transformation import *
try:
    list = ['A)', 'Б)', 'B)', 'Г)', 'Д)', 'Е)']
    print('A)a^3 & a^10, Б)a^4 & a^20, B)a^5 & a^13, Г)a^5 & a^19 Д)a^2, a^5 & a^17, Е)a^5 & a^19, Д)a^4, a^12 & a^28')
    permx = transform(float(input('Insert a number: ')))
    aNd = 'and'
    x = permx
    x*=x
    tempx = x
    x*=permx
    x1 = x
    x*=tempx
    x*=x
    print(list[0], x1, aNd, x)
    x=permx
    x*=x
    x*=x
    x1 = x
    x*=permx
    x*=x
    x*=x
    print(list[1], x1, aNd, x)
    x = permx
    x*=x
    tempx = x
    x*=permx
    tempx2 = x
    x*=tempx
    x1 = x
    x*=x
    x*=tempx2
    print(list[2], x1, aNd, x)
    x = permx
    x*=x
    x*=x
    tempx = x
    x*=permx
    x1 = x
    tempx*=x
    x*=x
    x*=tempx
    #impossible to do within 5 interations, even asked Google to do it, minimum is 6
    print(list[3], x1, aNd, x)
    x = permx
    x*=x
    x1 = x
    tempx2 = x
    x*=x
    x*=permx
    x2 = x
    tempx = x
    x*=x
    x*=tempx
    x*=tempx2
    print(list[4], x1, x2, aNd, x)
    x = permx
    x*=x
    x*=x
    x1 = x
    tempx = x
    x*=x
    x*=tempx
    x2 = x
    x*=x
    x*=tempx
    print(list[5], x1, x2, aNd, x)
except ValueError:
    print('Not a number!')