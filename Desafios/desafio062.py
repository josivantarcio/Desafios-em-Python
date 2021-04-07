pTermo = int(input('Informe Primeiro Termo: '))
razao = int(input('Informe a Razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont != total:
        print('{} . '.format(pTermo),end='')
        pTermo += razao
        cont += 1
    print()
    mais = int(input('Quantos Termos voce quer mostrar a mais? '))
print(total)