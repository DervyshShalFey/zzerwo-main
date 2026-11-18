try:
    x = int(input('Seconds(starts at 12:00 pm): '))
    if x < 0:
        raise Exception
    while x>= 86400:
        x-=86400
    print(f'Hours: {x//3600}')
    while x>= 3600:
        x-=3600
    print(f'Minutes: {x//60}')
    while x>= 60:
        x-=60
    print(f'Seconds: {x}')
except ValueError:
    print('Not a whole number!')
except Exception:
    print('Number can\'t be negative!')