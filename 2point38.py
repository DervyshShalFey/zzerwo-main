from th import *

listy = []
x = 101
while x < 150:
    listy.extend(str(x))
    x+=1

try:
    print('Given a number that consistes of numbers between 101 and 150. (101102103...149150). Insert k which will show u info about k-th numeral os that number.')
    k = int(input('Insert whole number between 1 to 150: '))
    if k<0 or k>150:
        raise Exception
    print(f'{th(k)} is: {listy[k-1]}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of range!!!')