from random import randint
def sortear(x):
    """Recebe os numeros inteiros do programa principal e coloca dentro de uma lista.
    by: Josevan Oliveira josivantarcio@gmail.com

    Args:
        x (int): n
    """
    nLista.append(x)
def somarPares(y):
    """Recebe o valor da lista criada da função sortear, 
    faz uma varredura dentro de um laço e seleciona somente os numeros pares da lista e realiza a soma.

    Args:
        y (list): nLista
    """
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

help(sortear)