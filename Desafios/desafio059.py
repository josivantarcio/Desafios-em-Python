n1 = int(input('Digite número 1: '))
n2 = int(input('Digite número 2: '))
menu = 0
while menu != 5:
    print('''Digite:
    [1] - Somar;
    [2] - Multiplicar;
    [3] - Maior;
    [4] - Novos Números;
    [5] - Sair do Programa.''')
    menu = int(input())
    if menu == 1:
        print('Soma: {}'.format(n1 + n2))
    elif menu == 2:
        print('Multiplicação: {} '.format(n1 * n2))
    elif menu == 3:
        n1 > n2 if print('O primeiro é maior!') else print('O Segundo é Maior!')
    elif menu == 4:
        n1 = int(input('Digite número 1: '))
        n2 = int(input('Digite número 2: '))
print('FIM')


