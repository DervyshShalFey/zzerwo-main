try:
    a = int(input('Insert first natural number:'))
    if a < 1:
        raise Exception
    b = int(input('Insert second natural number:'))
    if b < 1:
        raise Exception
    print(int((((a%b)*(b%a)+1))))
except Exception:
    print('You have inserted not a natural number!')