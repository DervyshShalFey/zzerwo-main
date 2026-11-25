
try:
    th = 0
    tm = 0
    h = int(input('Insert hours: '))
    if h > 12 or h < 0:
        raise Exception
    
    m = int(input('Insert minutes: '))
    if m > 59 or m < 0:
        raise Exception

    dh = h * 30 + m/2
    dm = m * 6

    while dh
    print(f'Degrees between 0 and hour arrow: {x}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of the range!!!')