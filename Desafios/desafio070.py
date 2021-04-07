total = conteMaiorqMil = 0
cont = 0
while True:
    prod = str(input('Nome do Produto: ')).strip().title()
    preco = float(input(f'Preço do {prod} R$: '))
    total += preco
    cont += 1

    if(cont == 1 or preco < menorPreco):
        menorPreco = preco
        menorProd = prod

    if(preco > 1000):
        conteMaiorqMil += 1
    while True:
        i = str(input('Deseja continuar? ')).strip().lower()[0]
        if(i in 'Ss' or i in 'Nn'):
            break
    if(i in 'Nn'):
        break

print(f'O total gasto foi de R${total:.2f}; Itens: {cont}\n'
      f'Possui {conteMaiorqMil} produtos acima de R$ 1000,00;\n'
      f'O produto mais barato foi: {menorProd}, custando R${menorPreco:.2f}')
