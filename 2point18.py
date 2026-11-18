
try:
    y = True
    x = int(input('Insert a number with three different digits: '))
    if x < 0:
        y = False
        x*=-1
    listx = list(str(x))
    if len(listx) != 3:
        raise Exception
    if len(listx) != len(set(listx)):
        raise ZeroDivisionError
    listx = list(map(lambda x: int(x), listx))
    setx = set()
    setx.add(listx[0] * 100 + listx[1] * 10 + listx[2])
    setx.add(listx[0] * 100 + listx[2] * 10 + listx[1])
    setx.add(listx[1] * 100 + listx[2] * 10 + listx[0])
    setx.add(listx[1] * 100 + listx[0] * 10 + listx[2])
    setx.add(listx[2] * 100 + listx[0] * 10 + listx[1])
    setx.add(listx[2] * 100 + listx[1] * 10 + listx[0])
    print(f'All results: {str(setx).strip('{}')}')
except ValueError:
    print('Not a whole number!')
except ZeroDivisionError:
    print('Digits must be different!')
except Exception:
    print('It must be a three-digit number!')