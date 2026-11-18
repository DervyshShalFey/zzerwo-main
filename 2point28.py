print('That\'s just replacing')
x = 546
listx = list(str(x))
listx = list(map(lambda x: int(x), listx))
x = listx[1]*100 + listx[0]*10 + listx[2]
print(x)