peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / altura ** 2
if(imc < 18.5):
    print('Abaixo do Peso!')
elif(imc >= 18.5 and imc < 25.0):
    print('Peso Ideal')
elif(imc >= 25.0 and imc < 30.0):
    print('Sobrepeso')
elif(imc >= 30.0 and imc < 40.0):
    print('Obesidade')
else:
    print('Obesidade Mórbida')
print('{:.2f}'.format(imc))