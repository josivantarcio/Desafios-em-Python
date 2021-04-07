soma = contador = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'A soma deu {soma} e foram {contador} numeros digitados')