from random import randint
from time import sleep
n = int(input('Quantos jogos? '))
jogos = []
bola = 0
bolao = []
for i in range(n):
    jogos.clear()
    for j in range(6):
            while bola in jogos or bola == 0:
                bola = randint(1, 60)
            jogos.append(bola)
    jogos.sort()
    print(jogos)
    sleep(1.5)
    bolao.append(jogos[:])