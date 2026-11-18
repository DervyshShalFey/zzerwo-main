from transformation import *
try:
    x = float(input('Meters: '))
    if x < 0:
        raise Exception
    x = transform(x)
    print(f'Kilometers: {transform(x//10)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative!')