try:
    print('2 numbers: a2a1 and b')
    a2 = int(input('Insert numeral a2: '))
    if a2 < 0 or a2 > 9:
        raise ValueError

    a1 = int(input('Insert numeral a1: '))
    if a1 < 0 or a1 > 9:
        raise ValueError

    b = int(input('Insert numeral b: '))
    if b < 0 or b > 9:
        raise ValueError

    if a2 == 9 and a1+a2 > 9:
        raise Exception
    x = a1 + b
    if x > 9:
        x-=10
        a2+=1

    print(f'Numeral of sum of a2a1 and b: {a2} and {x}')
except ValueError:
    print('Numerals must be numbers from 0 to 9!')
except Exception:
    print('Sum must be a 2-digit number!')