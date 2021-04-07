from random import randint
vitoria = 0
while True:
    cpu = randint(0, 10)
    while True:
        eJogador = str(input('Par ou Impar? ')).strip().lower() #escolha jogador
        if eJogador in 'par' or eJogador in 'impar':
            break
    nJogador = int(input('Digite um numero: '))
    soma = cpu + nJogador
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    if eJogador == resultado:
        vitoria += 1
    else:
        print(f'Você Perdeu! {cpu} + {nJogador} = {soma}. E ele é {resultado.title()}!')
        break
print(f'Total de Vitória(s): {vitoria}')