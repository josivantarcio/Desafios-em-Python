frase = str(input('Digite uma frase: '))
frase = frase.lower().strip()
print('A frase possui {} letras A.'.format(frase.count('a')))
print('Aparece a primeira na posicao {}.'.format(frase.find('a')))
print('Aparece a ultima na posicao {}.'.format(frase.rfind('a')))
