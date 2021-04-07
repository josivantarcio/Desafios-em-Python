jogador = {}
jogadores = []
gol = []
while True:
    jogador['nome'] = str(input('Nome: ')).strip().title()
    jogador['quantPartidas'] = int(input("Número de partidas de {}: ".format(jogador['nome'])))
    for i in range(jogador['quantPartidas']):
        jogador['partida'+str(i+1)] = int(input(f'Quantos gols fez {jogador["nome"]} na {i+1}ª partida: '))
        gol.append(jogador['partida'+str(i+1)])
    jogador['totalGols'] = sum(gol)
    jogador['golsPartidas'] = gol[:]
    gol.clear()
    jogadores.append(jogador.copy())
    while True:
        stp = str(input('Deseja continuar? S/N ')).strip().lower()[0]
        if stp in 'sn':
            break
        else:
            print('ERRO! Favor Digitar "S" ou "N" ')
    if stp == 'n':
        break
print('=' * 56)
for k, i in enumerate(jogadores):
    k += 1
    print(f" ==> Jogador nr {k}: {i['nome']:<6} jogou {i['quantPartidas']} partidas e fez {i['totalGols']} Gols.")
while True:
    nJogador = int(input('Qual Jogador deseja ver os detalhas? \033[1;31m"0 sair!"\033[m '))
    if nJogador == 0:
        break
    elif nJogador > len(jogadores):
        print(f'\033[1;33mQuantidade máxima de jogadores: {len(jogadores)}\033[m')
    else:
        for k, i in enumerate(jogadores):
            k += 1
            if nJogador == k:
                print("=" * 35)
                print(f"Historico do Jogador {i['nome']}")
                for x in range(i['quantPartidas']):
                    print(f'>>>   {x+1}ª partida fez {i["golsPartidas"][x]} gols')
                print(f"Total:============== {i['totalGols']}")
print('FIM')