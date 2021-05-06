from utilidadesCeV import dados, moeda
v = dados.leiaDinheiro('Digite um valor R$')
a = int(input('Acrescimo %' ))
d = int(input('Reducao %' ))
moeda.resumo(v,a,d)