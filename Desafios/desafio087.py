tab = [[],[],[]]
soma = somaTerceira = maior =  0
for i in range(3):
    for j in range(3):
        tab[i].append(int(input(f'Digite o valor da posição [{i}][{j}]: ')))

        if tab[i][j] % 2 == 0:
            soma += tab[i][j]
        if j == 2:
            somaTerceira += tab[i][j]
        if i == 1:
            if j == 0 or tab[i][j] > maior:
                maior = tab[i][j]
for i in range(3):
    for j in range(3):
        print(f'[{tab[i][j]:^5}]', end=' ')
    print()
print(f'A soma dos pares: {soma}')
print(f'A Soma da Terceira coluna é: {somaTerceira}')
print(f'O Maior número da segunda coluna é: {maior}')