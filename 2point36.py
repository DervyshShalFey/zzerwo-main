try:
    print('2 numbers: a3a2a1 and b2b1')

    a3 = int(input('Insert numeral a3: '))
    if a3 < 0 or a3 > 9:
        raise ValueError

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

    x = a1 + b1
    y = a2 + b2
    if x > 9:
        x-=10
        y+=1
    if y > 9:
        y-=10
        a3+=1
    if a3 > 9:
        raise Exception
    print(f'Numerals of sum of a2a1 and b: {a3}, {y} and {x}')
except ValueError:
    print('Numerals must be numbers from 0 to 9!')
except Exception:
    print('Sum must be a 3-digit number!')