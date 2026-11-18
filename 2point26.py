print('Pretty sure, u swap the numbers. I am a genius!')
print('Explanation, lets make our number x*100+y*10+z, we get rid of x, and multiplying by 10 so y*100+z*10 and then add x, so yea... ')
print('Proof(view code): ')
x = 564
listx = list(str(x))
listx = list(map(lambda x: int(x), listx))
x = x - listx[-1]
x /= 10
x += 100 * listx[-1]
print(int(x))
