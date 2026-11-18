try:
    x = int(input('Idk view 2point28, I am too lazy to explain. Well except you choose a number. Rules are that: it is more than or equal to 100, but less or equal to 999 and its 2nd number can\'t be zero. Well, insert it, I guess: '))
    if x > 999 or x < 100:
        raise Exception
    listx = list(str(x))
    if listx[1] == '0':
        raise ZeroDivisionError
    listx = list(map(lambda x: int(x), listx))
    x = listx[1]*100 + listx[0]*10 + listx[2]
    print(f'Result: {int(x)}')
except ValueError:
    print('You have inserted not a whole number!')
except ZeroDivisionError:
    print('Last number can\'t be zero, I guess I told ya?')
except Exception:
    print('Number must be more than or equal to 100, but be less or equal to 999!')