try:
    a = int(input('Insert first natural number:'))
    b = int(input('Insert second natural number:'))
    print(int((((a%b)*(b%a)+1))))
except ValueError:
    print('You have inserted not a natural number!')