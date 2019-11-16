from random import random
print('До:')
M = 5
N = 5
a = []
c = 0
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*100)-50
        b.append(n)
        print('%4d' % n, end='')
    print()
    a.append(b)
print()

print('После:')
for i in range(N):
    a[i][i] = 0
    print(a[c])
    c = c + 1