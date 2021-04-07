tab = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        tab[i][j] = (int(input(f'Digite um numero na posicao [{i}][{j}]: ')))
for i in range(3):
    for j in range(3):
        print(f'[{tab[i][j]:^5}]',end=' ')
    print()