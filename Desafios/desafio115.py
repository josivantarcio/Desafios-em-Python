from utilidadesCeV.menu import *
from utilidadesCeV.arquivo import *


Arq = 'Desafios\\arquivo01Exercicio115.txt'
if arquivoExiste(Arq):
    print('Arquivo Localizado.')
else:
    criarArquivo(Arq)
    print(f'Arquivo {Arq} Criado com Sucesso.')
    

while True:
    n = menu(['Cadastrar Pessoas','Lista de Pessoas','Sair do Sistema'])
    if n == 3:
        final()
        break
    elif n == 1:
        cabecalho('Cadastrar Pessoas')
        nome = str(input('Nome: ')).title().strip() 
        idade = leiaInt('Idade: ')
        cadastrarPessoa(Arq, nome, idade)
    elif n == 2:
        cabecalho('Lista de Pessoas')
        lerArquivo(Arq)
    else:
        cabecalho('Opção Invalida!')