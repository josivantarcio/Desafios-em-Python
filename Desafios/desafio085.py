lista = [[],[]]
for i in range(7):
    n = (int(input(f'Digite o numero {i+1}: ')))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Lista dos pares {lista[0]}\nLista dos impares {lista[1]}')