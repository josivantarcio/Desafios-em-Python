preco = float(input('Valor do Produto: R$'))
formaPagamento = str(input('Forma de Pagamento: ')).strip()

if 'a vista' in formaPagamento:
    formaVista = str(input('Cartão, Dinheiro ou Cheque?\n')).strip()
    if 'cartao' not in formaVista:
        precofinal = preco - preco * 10 / 100
    else:
        precofinal = preco - preco * 5 / 100
else:
    parcela = int(input('Quantidade de Parcelas: '))
    if(parcela == 2):
        precofinal = preco
    else:
        precofinal = preco + preco * 20 / 100
    parcela = precofinal/parcela
    print('O valor da parcela R$ \033[1;31m{:.2f}\033[m'.format(parcela))
print(formaPagamento)
print('O valor final foi de R$ \033[1;33m{:.2f}\033[m'.format(precofinal))

