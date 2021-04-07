#an = a1 + (n - 1) * r

a1 = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
an = a1 + (10 - 1) * r
for i in range(a1, an + r, r):
    print(i,end=' ')
