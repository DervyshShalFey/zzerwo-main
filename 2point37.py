from th import *
def isodd(x):
    if x % 2 == 0:
        return x/2
    else:
        return (x/2)+1

listx = []
listy = []
x = 10
while x < 100:
    listx.append(x)
    listy.extend(str(x))
    x+=1

try:
    print('Given a number that consistes of numbers between 10 and 99. (101112...9899). Insert k which will show u info about k-th numeral os that number.')
    k = int(input('Insert whole number between 1 to 180: '))
    if k<0 or k>180:
        raise Exception
    k-=1
    print(f'{th(k+1)} is {iseven(k+1)} meaning its pair is {th(int(isodd(k+1)))}, numeral of that big number is {listy[k]} and its pair number is {listx[(int(isodd(k-1)))]}')
except ValueError:
    print('You have inserted not a whole number!')
except Exception:
    print('You have inserted a number outside of range!!!')