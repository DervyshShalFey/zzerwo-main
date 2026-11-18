from transformation import *
try:
    x = float(input('Centimeters: '))
    if x < 0:
        raise Exception
    x = transform(x)
    print(f'Meters: {transform(x//100)}')
except ValueError:
    print('Not a number!')
except Exception:
    print('Number can\'t be negative!')