from transformation import *
try:
    x = module(int(input('Insert a number with three digits: ')))
    listx = list(str(x))
    if len(listx) != 3:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print(f'A) Your number has {listx[2]} ones in it')
    print(f'Б) Your number has {listx[1]} tens in it')
    print(f'B) Sum of digits in your number is equal to {listx[0]+listx[1]+listx[2]}')
    print(f'Г) Product of digits in your number is equal to {listx[0]*listx[1]*listx[2]}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a three-digit number!')