salario = float(input('Digite o valor do funcionario R$: '))
if(salario <= 1250):
    salario = salario + salario * 0.15
else:
    salario = salario + salario * 0.10
print('O Salario do Funcionario será de R$:{:.2f}'.format(salario))
