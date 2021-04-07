r1 = float(input('Lado 1: '))
r2 = float(input('Lado 2: '))
r3 = float(input('Lado 3: '))
if(r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('É triangulo!')
else:
    print('Não é triangulo')