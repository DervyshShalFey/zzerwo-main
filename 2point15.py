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
    print('What if we cross out last number and write it at the start?')
    x = listx[2] * 100 + listx[0] * 10 + listx[1]
    print(f'Result: {ifneg(x, y)}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a three-digit number!')