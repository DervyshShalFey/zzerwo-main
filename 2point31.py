try:
    x = int(input('Idk view 2point28, I am too lazy to explain. Well except you choose a number. Rules are that: it is more than or equal to 100, but less or equal to 999. Well, insert it, I guess: '))
    if x > 999 or x < 100:
        raise Exception
    listx = list(str(x))
    listx = list(map(lambda x: int(x), listx))
    x = listx[0]*100 + listx[2]*10 + listx[1]
    print(f'Result: {int(x)}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('Number must be more than or equal to 100, but be less or equal to 999!')