from transformation import *
from th import *
try:
    x = module(int(input('Insert a whole number. It must be greater than ninety nine: ')))
    listx = list(str(x))
    if x <= 99:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print(f'A) Your number has {listx[-2]} {add_s(int(listx[-2]), 'ten')} in it')
    print(f'Б) Your number has {listx[-3]} {add_s(int(listx[-3]), 'hundred')} in it')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('Number must be greater than ninety nine!')