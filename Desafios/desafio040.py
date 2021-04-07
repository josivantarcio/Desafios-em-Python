nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))
media = (nota1 + nota2) / 2
if(media < 5.0):
    print('Média abaixo de \033[1;33m5.0:\n\033[1;31mREPROVADO')
elif(media >= 5.0 and media <= 7):
    print('Média entre de 5.0 e 6.9\033[1;33m:\nRECUPERAÇÃO')
elif(media >=7.0 and media <=10.0):
    print('Média entre de 7.0 e 10.0\033[1;33m\n\033[1;34mAPROVADO')