a = []
while True:
    a.append(int(input('Digite o valor: ')))
    st = str(input('Deseja continuar? S/N ').strip()[0].lower())
    if st in 'n':
        break

a.sort(reverse=True)
if 5 in a:
    print(f'O número 5 faz parte da lista e aparece {a.count(5)} vezes!')
else:
    print('O número 5 não faz parte da lista')

print(f'{len(a)} -> quantidade de números')
print(f'{a} -> do maior para o menor')
