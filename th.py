def th(x):
    if x == 1 or x%100==1:
        return f'{x}st number'
    elif x == 2 or x%100==2:
        return f'{x}nd number'
    elif x == 3 or x%100==3:
        return f'{x}rd number'
    else:
        return f'{x}th number'
def iseven(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd' 