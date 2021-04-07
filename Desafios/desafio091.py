from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
for k, v in jogo.items():
    print(f'{k} jogou {v}')
    sleep(0.5)
rk = {}
rk = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('='*24)
print('     == Ranking ==')
for i, v in enumerate(rk):
    sleep(1)
    print(f'{i+1}ºLugar,{v[0]} tirou {v[1]}')





