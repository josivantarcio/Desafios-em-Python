def fatorial(n, show=False):
    """Faz o calculo do fator de um numero inteiro

    Args:
        n (int): numero para calcular o fator
        show (bool, optional): Mostra detalhamento do calculo. Defaults to False.
    """
    from time import sleep
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show == True: 
            if i == 1:
                print(i, end= ' = ',flush=True)
            else:
                print(i, end=' x ', flush=True)
            sleep(0.7)
    print(f)


n = int(input('Digite um numero '))
shw = str(input('Mostrar? S/N ')).upper()[0]
if shw == 'S':
    show = True
else:
    show = False
fatorial(n, show)