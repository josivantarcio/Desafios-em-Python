def arquivoExiste(msg):
    try:
        a = open(msg, 'rt')
        return True
    except FileNotFoundError:
        return False
    
def criarArquivo(msg):
    try:
        a = open(msg, 'wt+')
    except FileExistsError:
        print('Nao foi possivel criar o arquivo!')
        
def lerArquivo(msg):
    try:
        a = open(msg, 'rt')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<15} tem {dado[1]:>3} anos')
    except FileNotFoundError:
        print(f'Impossivel Ler Arquivo {msg}')
        
def cadastrarPessoa(msg, nome='none',idade=0):
    try:
        a = open(msg, 'at')
        a.writelines(f'{nome};{idade:>4}\n')
        print(f'Novo registro de {nome} adicionado com sucesso!')
    except FileExistsError:
        print(f'Não foi possivel gravar informacoes do arquivo {msg}!')        