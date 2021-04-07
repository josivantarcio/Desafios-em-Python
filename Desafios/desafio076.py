prod = (input('Digite produto: '),input('Digite o Preco: '),
        input('Digite produto: '),input('Digite o Preco: '),
        input('Digite produto: '),input('Digite o Preco: '),
        input('Digite produto: '),input('Digite o Preco: '))

print('=' * 29)
print('Tabela de Preço')
print('=' * 29)

for i in range(len(prod)):
    if i % 2 == 0:
        print(f'{prod[i]:.<23}',end='')
    else:
        print(f'R${prod[i]}')



