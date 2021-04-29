def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade <= 64:
        situacao = 'Obrigatório'
    elif idade < 16:
        situacao = 'Negado'
    else:
        situacao = 'Opcional'
    return f'{situacao}, {idade} anos'

anoNascimento = int(input('Digite o ano de nascimento: '))
voto(anoNascimento)
print(f'O cidadão tem situacao nas eleições desse ano como: {voto(anoNascimento)}')