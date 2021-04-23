from random import randint
def sortear(x):
    nLista.append(x)
def somarPares(y):
    somar = 0
    for i in y:
        if i % 2 == 0:
            somar += i
    print(f'A soma dos pares = {somar}')
            
    
#main
nLista = []
for i in range(5):
    n = randint(1,100)
    sortear(n)
print(f'Lista composta por {nLista}')
somarPares(nLista)