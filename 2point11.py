from time import sleep
def ifneg(x, y):
    if y == False:
        x*=-1
    return x
try:
    y = True
    x = int(input('Insert a number with two digits: '))
    if x < 0:
        y = False
        x*=-1
    listx = list(str(x))
    if len(listx) != 2:
        raise Exception
    listx = list(map(lambda x: int(x), listx))
    print('Shuffling...')
    sleep(3)
    print('Shuffled!')
    x = listx[1] * 10 + listx[0]
    print(f'Result: {ifneg(x, y)}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('It must be a two-digit number!')