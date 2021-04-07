frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
juntarPalavras = ''.join(palavras)
trocar = juntarPalavras[::-1]
print(trocar)