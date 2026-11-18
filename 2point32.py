print('That\'s just replacing')
x = 654
listx = list(str(x))
listx = list(map(lambda x: int(x), listx))
x = listx[2]*100 + listx[1]*10 + listx[0]
print(x)