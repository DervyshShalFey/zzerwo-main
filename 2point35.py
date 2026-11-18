try:
    print('2 numbers: a2a1 and b2b1')
    a2 = int(input('Insert numeral a2: '))
    if a2 < 0 or a2 > 9:
        raise ValueError

    a1 = int(input('Insert numeral a1: '))
    if a1 < 0 or a1 > 9:
        raise ValueError

    b2 = int(input('Insert numeral b2: '))
    if b2 < 0 or b2 > 9:
        raise ValueError

    b1 = int(input('Insert numeral b1: '))
    if b1 < 0 or b1 > 9:
        raise ValueError

    if (b2+a2 > 9) or (b2+b1 == 9 and b1+a1 > 9):
        raise Exception
    x = a1 + b1
    y = a2 + b2
    if x > 9:
        x-=10
        y+=1

    print(f'Numeral of sum of a2a1 and b: {y} and {x}')
except ValueError:
    print('Numerals must be numbers from 0 to 9!')
except Exception:
    print('Sum must be a 2-digit number!')