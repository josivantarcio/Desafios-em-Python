import moeda
num = float(input('Digite um valor R$: '))
var = int(input('Variação: '))
print(moeda.aumentar(num, var))
print(moeda.diminuir(num, var))
print(moeda.metade(num))
print(moeda.dobro(num))