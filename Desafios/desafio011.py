a = float(input('digite a altura (M) '))
l = float(input('digite a largura (M) '))
area = a * l
tinta = 2
areaPintada = area /tinta
print('A area é de {:.2f}M² e Precisa de {:.2f}l de tinta para pintar!'.format(area,areaPintada))