valores = list()

for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(valores)