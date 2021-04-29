from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade >= 18 and idade <= 64:
        situacao = 'Obrigatório'
    elif idade < 16:
        situacao = 'Negado'
    else:
        situacao = 'Opcional'
    return situacao, idade

anoNascimento = int(input('Digite o ano de nascimento: '))
voto(anoNascimento)
print(f'O cidadão com tem situacao nas eleições desse ano como: {voto(anoNascimento)}')