
print('That\'s just replacing')
x = 456
listx = list(str(x))
listx = list(map(lambda x: int(x), listx))
x = listx[0]*100 + listx[2]*10 + listx[1]
print(x)