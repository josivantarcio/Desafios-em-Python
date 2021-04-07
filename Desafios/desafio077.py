lista = ('carro','moto','trator','caminhao','coracao','ovo',
         'mao','paralelepipedo','borboleta','onibus','Brasil','papai')
for i in lista:
    print(f'\nA palavra {i}, possui as vogais: ',end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')