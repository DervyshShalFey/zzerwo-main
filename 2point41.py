from transformation import *
from math import *
from th import *
try:
    x = radians(int(input('Insert number of degrees on clock between a ray passing through line that consists of 12 and 6 hours on clock and hour arrow (0<=x<=2π): ')))

    if x >= 360 or x <= 0:
        raise Exception
    
    h = round(module((6 * x) / pi))
    m = round(module(((360 * x) / pi) - 60 * h))
    a = module(round(degrees(12 * x - 2 * pi * h)))
    print(f'{h} {add_s(h, 'hour')} and {m} {add_s(m, 'minute')} have passed!')
    print(f'Degrees between that line and minute arrow: {a}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of the range!!!')