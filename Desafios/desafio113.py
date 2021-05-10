def printErro():
    print('\033[31mErro! Digite um numero valido\033[m')

def leiaInt(n=0):
    while True:
        try:
            valor = int(input(n))
            break
        except (ValueError, TypeError):
            printErro()
    return valor
    
def leiaReal(r):
    for i in range(2, -1, -1):
        try:
            valor = float(input(r))
            return valor
            break
        except (ValueError, TypeError, EOFError):
            printErro()
            print(f'Voce tem {i} tentativas restantes')
        except (KeyboardInterrupt, KeyError):
            print('\nErro! Programa suspenso pelo usuario')
            return 0
            break
    print('Fim das tentativas! Inicie novamente')
    
n = leiaInt('Digite um numero inteiro: ')
f = leiaReal('Digite um numero real: ')
print(f'O numero inteiro foi {n} e o real {f}')