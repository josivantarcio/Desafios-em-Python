import random
import time
armas = ('pedra','papel','tesoura')
nome = str(input('Digite seu nome: ')).upper()
print('''Escolha sua arma {}!
[ 0 ] - Para \033[1;34mPedra\033[m;
[ 1 ] - Para \033[1;34mPapel\033[m;
[ 2 ] - Para \033[1;34mTesoura\033[m
[ 9 ] - Para \033[1;31mFinalizar\033[m;'''.format(nome))
jogador = int(input(':_'))
print('é (1)...',end='')
time.sleep(0.5)
print('(2)...',end='')
time.sleep(0.5)
print('(3)...',end='')
time.sleep(0.5)
print('eee JÁ!!!\n')
time.sleep(1)
wj = 0
wc = 0
while jogador != 9:
    cpu = random.randint(0, 2)
    if cpu == 0: ##pedra
        if jogador == 0: #pedra
            print('EMPATE')
        elif jogador == 1: #papel
            print('JOGADOR WIN')
            wj += 1
        elif jogador == 2: #tesoura
            print('CPU WIN')
            wc += 1
    elif cpu == 1: ##papel
        if jogador == 0: #pedra
            print('CPU WIN')
            wc += 1
        elif jogador == 1: #papel
            print('EMPATE')
        elif jogador == 2: #tesoura
            print('JOGADOR WIN')
            wj += 1
    elif cpu == 2: ##tesoura
        if jogador == 0: #pedra
            print('JOGADOR WIN')
            wj += 1
        elif jogador == 1: #papel
            print('CPU WIN')
            wc += 1
        elif jogador == 2: #tesoura
            print('EMPATE')
    print('='*15)
    print('CPU X {}'.format(nome))
    jogador = int(input(':_'))
    print('é (1)...',end='')
    time.sleep(0.5)
    print('(2)...',end='')
    time.sleep(0.5)
    print('(3)...',end='')
    time.sleep(0.5)
    print('eee JÁ!!!\n')
    time.sleep(1)
print('Fim do Jogo!')
print('CPU X {}'.format(nome))
print('{} X {}'.format(wc,wj))