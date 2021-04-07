lista = list()
pares = list()
impares = list()
while True:
    lista.append((int(input("Digite um valor: "))))
    stp = str(input('Deseja continuar? S/N ').lower()[0].strip())
    if stp in 'n':
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(lista)
print(f'Impares -> {impares}')
print(f'Pares -> {pares}')