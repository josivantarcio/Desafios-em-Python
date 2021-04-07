vel = float(input('Velocidade do veículo: '))
velMax = 80
taxa= 7.00
if(vel > velMax):
    multa = (vel - velMax) * taxa
    print('Você ultrapassou o limite de velocidade! Pagar multa de R${:.2f}'.format(multa))
print('Dirija com Cuidado!')