def valores(i):
    cont = len(i)
    for j in i:
        print(j, end=' ')
    print(f'Forem informado(s) {cont} número(s)!')
    print(f'O Maior é {max(i)}')
    

from random import randint
#main
numLista = []
numeros = randint(1,9)
for i in range(numeros):
    n = randint(0,100)
    numLista.append(n)
valores(numLista)        