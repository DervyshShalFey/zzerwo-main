from th import *
try:
    h = 0
    m = 0
    x = int(input('Insert number of degrees on clock that hour arrow has passed (0<=x<=360): '))

    if x >= 360 or x <= 0:
        raise Exception
    
    while x >= 30:
        x-=30
        h+=1

    while x >= 2:
        x-=2
        m+=1
    print(f'{h} {add_s(h, 'hour')} and {m} {add_s(m, 'minute')} have passed!')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of the range!!!')