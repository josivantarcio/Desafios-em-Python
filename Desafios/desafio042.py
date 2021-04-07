l1 = float(input('Digite lado 1: '))
l2 = float(input('Digite lado 2: '))
l3 = float(input('Digite lado 3: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 >l2:
    if l1 == l2 == l3:
        print('Triangulo Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
else:
    print('Não é um Triangulo')