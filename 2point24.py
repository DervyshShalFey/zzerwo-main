print('To solve this problem we need to do MATHS, yes MATHS, it is an extremely hard lesson, but yet we have to use it. :\'( ')
print('FIRST, we have to find a number to start with. In my humble opinion it is', 237, ' . You may have differemnt one, but I don\'t give a DAMN ahahahhahahahah')
print('alr I will stop messing around. last number is 7, because it is last and we subtract the starting number so we basically doing \'x-x\' equation, and we always get 0. Since we write 7 as the last one, this is it ')
print('we take away 7 and are getting 23, we multiply it by 10 getting 230. and adding 7 sop 237? So it is the same? Yea, it is, even if we replace 237 with 456 o5r smth')
print('Well, here is the result: ')
x = 237
listx = list(str(x))
x = (x - int(listx[-1])) / 10
x = x * 10 + int(listx[-1])
print(int(x))
