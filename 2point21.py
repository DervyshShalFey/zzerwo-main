from transformation import *
try:
    x = module(int(input('Insert a whole number. It must be greater than nine: ')))
    listx = list(str(x))
    if x <= 9:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print(f'A) Your number has {listx[-1]} ones in it')
    print(f'Б) Your number has {listx[-2]} tens in it')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('Number must be greater than nine!')