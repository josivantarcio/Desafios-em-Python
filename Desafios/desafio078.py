numeros = list()
maiorPosicao = list()
menorPosicao = list()
for i in (range(5)):
    numeros.append(int(input('Digite o valor: ')))
    maior = max(numeros)
    menor = min(numeros)
for c, i in enumerate(numeros):
    if i == maior:
        maiorPosicao.append(c)
    if i == menor:
        menorPosicao.append(c)
print(f'Voce digitou os valores {numeros}')
print(f'{maior} é o maior número e está nas posicões {maiorPosicao}')
print(f'{menor} é o menor número e está nas posicões {menorPosicao}')