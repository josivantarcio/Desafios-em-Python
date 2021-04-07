numero = int(input('Digite um numero '))
print('Digite:\n [1] - para Binario;\n [2] - para Octal;\n [3] - para hexadecial')
escolha = int(input())
if escolha == 1:
    numero = bin(numero)
elif escolha == 2:
    numero = oct(numero)
elif escolha == 3:
    numero = hex(numero)
else:
    print('numero invalido')
print(numero[2:])
