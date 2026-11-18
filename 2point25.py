try:
    x = int(input('Idk view 2point24, I am too lazy to explain. Well except you choose a number. Rules are that: it is more than or equal to ten, but less or equal to 999 and its last number can\'t be zero. Well, insert it, I guess: '))
    if x >= 999 or x <= 10:
        raise Exception
    listx = list(str(x))
    if listx[-1] == '0':
        raise ZeroDivisionError
    x = (x - int(listx[-1])) / 10
    x = x * 10 + int(listx[-1])
    print(f'Result: {int(x)}')
except ValueError:
    print('You have inserted not a whole number!')
except ZeroDivisionError:
    print('Last number can\'t be zero, I guess I told ya?')
except Exception:
    print('Number must be more than or equal to 10, but be less or equal to 999!')