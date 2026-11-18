from transformation import *
try:
    x = module(int(input('Insert a number with four digits: ')))
    listx = list(str(x))
    if len(listx) != 4:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print(f'A) Sum of digits in your number is equal to {listx[0]+listx[1]+listx[2]+listx[3]}')
    print(f'Б) Product of digits in your number is equal to {listx[0]*listx[1]*listx[2]*listx[3]}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a four-digit number!')