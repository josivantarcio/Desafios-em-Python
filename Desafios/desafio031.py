distancia = float(input('Digite a distancia: '))
if(distancia <= 200):
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('valor da passagem: R${:.2f}'.format(valor))
