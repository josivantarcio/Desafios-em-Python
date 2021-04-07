n = int(input('Digite um numero: '))
i = 0
while n >= 0:
    while True:
        print(f'{i} x {n} = {i * n}')
        i += 1
        if i > 10:
            break
    i = 0
    n = int(input('Digite um numero: '))
print('FIM')
