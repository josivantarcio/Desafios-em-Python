n = int(input('Calculadora de: '))
op = str(input('''Operação: 
[ + ] - Soma;
[ - ] - Subtração;
[ * ] - Multiplicação;
[ / ] - Divisão;
[ P ] - Potência;
[ % ] - Resto.\n'''))
for i in range(0, 11):
    if '+' in op:
        print('{:2} + {} = {:2}'.format(i, n, i + n))
    elif '-' in op:
        print('{:2} - {} = {:2}'.format(i, n, i - n))
    elif '*' in op:
        print('{:2} x {} = {:2}'.format(i, n, i * n))
    elif '/' in op:
        print('{:2} / {} = {:2}'.format(i, n, i / n))
    elif 'P' in op:
        print('{:2} ** {} = {:2}'.format(i, n, i ** n))
    elif '%' in op:
        print('{:2} % {} = {:2}'.format(i, n, i % n))