import math
n = int(input())

d = [1]*(2*123456+1)

for i in range(2, int(math.sqrt(123456*2+1))):
    if d[i]:
        for j in range(i+i, len(d), i):
            d[j] = 0

while n!=0:
    print(d[n+1:2*n+1].count(1))
    n = int(input())