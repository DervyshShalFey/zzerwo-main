def matchcase1(x):
    match x:
        case 1: return 'January'
        case 2: return 'February'
        case 3: return 'March'
        case 4: return 'April'
        case 5: return 'May'
        case 6: return 'June'
        case 7: return 'July'
        case 8: return 'August'
        case 9: return 'September'
        case 10: return 'October'
        case 11: return 'November'
        case 0: return 'December'
try:
    x = int(input('Since the beggining of January 1990 n months and 2 days have passed. Insert n: '))
    if x < 0:
        raise Exception
    while x > 12:
        x-=12
    print(f'Month: {matchcase1(x%12+1)}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('Number can\'t be negative!')