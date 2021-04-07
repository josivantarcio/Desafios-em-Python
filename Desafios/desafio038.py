n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º número: '))
if n1 > n2:
    print('-O \033[1;33mprimeiro valor\033[m é \033[1;34mmaior\033[m')
elif n1 < n2:
    print('-O \033[1;33mseguundo valor\033[m é \033[1;34mmaior\033[m')
else:
    print('\033[1;33m- Não existe\033[m valor maior,os dois são \033[0;34miguais\033[m')