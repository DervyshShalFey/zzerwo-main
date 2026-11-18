
from transformation import *
import re
try:
    x = module(int(input('Insert a number with four digits: ')))
    listx = list(str(x))
    if len(listx) != 4:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print(f'A) Reversed: {listx[3] * 1000 + listx[2] * 100 + listx[1] * 10 + listx[0]}')
    print(f'Б) 1 and 2, 3 and 4 replaced: {listx[1] * 1000 + listx[0] * 100 + listx[3] * 10 + listx[2]}')
    print(f'B) 2 and 3 replaced: {listx[0] * 1000 + listx[2] * 100 + listx[1] * 10 + listx[3]}')
    print(f'Г, 1) First two and second two replaced: {listx[2] * 1000 + listx[3] * 100 + listx[0] * 10 + listx[1]}')
    listy = [listx[0], listx[1]]
    listz = [listx[2], listx[3]]
    print(f'Г, 2) {re.sub(r"[\[\], ]", "", str(listz + listy))}')

except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a four-digit number!')