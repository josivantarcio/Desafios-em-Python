from random import randint
for i in range(5):
    n = (randint(0,10))
    if(i == 0):
        m = n
        M = n
    if (n > M):
        M = n
    elif (n < m):
        m = n
    print(n, end=' ')
print(f'\nO maior número foi {M}\nE o Menor foi {m}')