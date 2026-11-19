#UNFINISHED
x = 0
try:
    h = int(input('Insert hours: '))
    if h > 23 or h < 0:
        raise Exception
    m = int(input('Insert minutes: '))
    if m > 59 or m < 0:
        raise Exception
    s = int(input('Insert seconds: '))
    if s > 59 or s < 0:
        raise Exception
    if h >= 6:
        m *= -1
        h *= -1
    x += h*30 + int(m/2)
    print(f'Degrees between 0 and hour arrow: {x}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of range!!!')