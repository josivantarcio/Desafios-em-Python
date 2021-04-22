def area(a, c):
    terreno = a * c
    print(f'A área do terreno é de {a} x {c} tem tamanho {terreno}m²')

#main
alt = float(input('Digite a altura: '))
comp = float(input('Digite o comprimento: '))
area(alt, comp)