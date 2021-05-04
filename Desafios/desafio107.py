import moeda
num = float(input('Digite um valor R$: '))
var = int(input('Variação: '))
moeda.aumentar(num, var)
moeda.diminuir(num, var)
moeda.metade(num)
moeda.dobro(num)