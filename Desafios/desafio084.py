pessoa = list()
t = []
maior = menor = 0
while True:
    t.append(str(input('Nome: ').title()))
    t.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = t[1]
    else:
        if t[1] > maior:
            maior = t[1]
        else:
            menor = t[1]
    pessoa.append(t[:])
    t.clear()
    stp = str(input('Deseja continuar? ')).lower()[0]
    if stp in 'n':
        break
del(t)
print(f'Total de pessoas: {len(pessoa)}')
print(f'O maior peso foi de {maior} para as pessoas',end=' ')
for i in pessoa:
    if i[1] == maior:
        print(i[0],end=' ')
print(f'\nO menor peso foi de {menor} para as pessoas',end=' ')
for i in pessoa:
    if i[1] == menor:
        print(i[0],end=' ')

