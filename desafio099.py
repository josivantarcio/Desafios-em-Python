def valores(i):
    cont = len(i)
    
    for j in i:
        print(j, end=' ')
    print(f'Forem informados {cont} numeros!')
    print(f'O Maior é {max(i)}')
    

from random import randint
#main
numeros = []
for i in range(6):
    n = randint(1,9)
    numeros.append(n)
    valores(numeros)
        