def ficha(nome='User', gol=0):
    """Tratando de erro no preenchimento de dados com numeros e nomes vazios.

    Args:
        nome (str, optional): Nome do Jogador digitado. Defaults to 'User'.
        gol (int, optional): Quantidade de gol do Jogador. Defaults to 0.
    """
    print(f'{nome} fez {gol}')


nome = str(input('Nome do Jogador: '))
gol = str(input('Gol Marcados: '))
if gol.isnumeric(): #isnumeric -> verifica se o dado é numero
    gol = int(gol) #converteu para inteiro
else:
    gol = 0
if nome == '':
    ficha(gol=gol)
else:
    ficha(nome,gol)