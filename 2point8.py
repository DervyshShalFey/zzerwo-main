
def matchcase1(x):
    match x:
        case 1: return 'Monday'
        case 2: return 'Tuesday'
        case 3: return 'Wednesday'
        case 4: return 'Thursday'
        case 5: return 'Friday'
        case 6: return 'Saturday'
        case 0: return 'Sunday'
def matchcase2(x):
    match x:
        case 0: return 'Monday'
        case 1: return 'Tuesday'
        case 2: return 'Wednesday'
        case 3: return 'Thursday'
        case 4: return 'Friday'
        case 5: return 'Saturday'
        case 6: return 'Sunday'
try:
    print('A)January 1st is Monday; Б)January 1st is Tuesday')
    x = int(input('Insert day since January 1st: '))
    x-=1
    if x <= 0:
        raise Exception
    if x > 365:
        raise SyntaxError
    print(f'A) Day of the week: {matchcase1(x%7)}')
    print(f'Б) Day of the week: {matchcase2(x%7)}')
except ValueError:
    print('Not a whole number!')
except SyntaxError:
    print('There can\'t be more than 366 days in a year!')
except Exception:
    print('Number can\'t be negative or be equal to zero!')