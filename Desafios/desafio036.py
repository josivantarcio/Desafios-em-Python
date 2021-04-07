valorCasa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário: R$ '))
duracao = 12 * int(input('Pagar em quantos meses: '))
parcela = valorCasa / duracao

if parcela > (salario*30/100):
    print('Infelizmente, seu crédito não foi aprovado')
    print('Valor da Parcela {:.2f}, é superior a '
          '30% do salário mensal: {}'.format(parcela, salario))
else:
    print('_-' * 20)
    print('Parabéns seu crédito foi aprovado. Ficará:')
    print('PARCELA: R${:.2f}\Mês\nDURACAO: {}'.format(parcela, duracao))

print('='*20)
print('\033[1;33mSalario: R${:.2f}'.format(salario))
print('\033[1;34m30% Salário: R${:.2f}'.format(salario*30/100))
print('\033[1;35mParcela: R${:.2f}\033[m'.format(parcela))
print('='*20)