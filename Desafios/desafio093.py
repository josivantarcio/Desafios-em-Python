jogador = dict()
jogador['nome'] = str(input('Nome: ')).strip().title()
nPartida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
soma = 0
for i in range(nPartida):
    jogador['partida'+ str(i+1)] = int(input(f'Quantos gols na partida {i+1} '))
    soma += jogador['partida'+str(i+1)]
jogador['totalGols'] = soma
print(' === APROVEITAMENTO ===')
for k, v in jogador.items():
    print(f' ==> {k}, tem valor {v}')