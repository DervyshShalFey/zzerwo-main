def ifneg(x, y):
    if y == False:
        x*=-1
    return x
try:
    y = True
    x = int(input('Insert a number with three digits: '))
    if x < 0:
        y = False
        x*=-1
    listx = list(str(x))
    if len(listx) != 3:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print('What if we exchange position of first and second number?')
    x = listx[1] * 100 + listx[0] * 10 + listx[2]
    print(f'Result: {ifneg(x, y)}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a three-digit number!')