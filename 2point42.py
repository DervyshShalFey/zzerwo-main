#UNFINISHED
from th import *
from transformation import *
try:
    th1 = 0
    tm = 0
    ts = 0
    h = int(input('Insert hours: '))
    if h > 12 or h < 0:
        raise Exception
    

    m = int(input('Insert minutes: '))
    if m > 59 or m < 0:
        raise Exception

    dh = int(h * 30 + m/2)
    dm = m * 6

    A = []
    B = []

    while not A and not B:
        ts+=1
        if ts >= 60:
            ts=0
            m+=1
            tm+=1

        if m>=60:
            m=0
            h+=1

        if tm>=60:
            tm=0
            th1+=1

        dh = h * 30 + m/2
        dm = m * 6 + ts / 10
        while dh >= 360:
            dh-=360
        while dm >= 360:
            dm-=360
        if dh == dm:
            A += [th1, tm]
        if module(dh-dm) == 90:
            B += [th1, tm]
    
    print(f'A) {A[0]} {add_s(A[0], 'hour')} and {A[1]} {add_s(A[1], 'minute')} need to pass before arrows will face the same direction!')
    print(f'A) {A[0]} {add_s(A[0], 'hour')} and {A[1]} {add_s(A[1], 'minute')} need to pass before arrows will face the same direction!')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of the range!!!')