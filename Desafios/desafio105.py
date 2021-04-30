def notas(n, situacao=False):
    """funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A media da turma
    - A situacao (opcional)
    
    Args:
        n (list): receberar a lista apos o sistema receber o numero zero
        situacao (bool, optional): Sera calculado a situacao mediante a media. Defaults to False.

    Returns:
        dict: envia para a variavel resultado e imprime no final
    """
    aluno = {}
    aluno['quantNotas'] = len(n)
    aluno['maiorNota'] = max(n)
    aluno['menorNota'] = min(n)
    aluno['mediaNotas'] = sum(n) / len(n)
    if situacao == True:
        if aluno['mediaNotas'] >= 9:
            aluno['situacao'] = 'Otima'
        elif aluno['mediaNotas'] >= 7:
            aluno['situacao'] = 'Boa'
        elif aluno['mediaNotas'] >= 5:
            aluno['situacao'] = 'Ruim'
        else:
            aluno['situacao'] = 'Péssima'
    return aluno
    

#main
temp = []
while True:
    n = float(input('Digite a nota: '))
    if n == 0:
        break
    if 0 <= n <= 10:
        temp.append(n)
## situacao 
sit = str(input('Deseja ver a situacao? S/N ')).upper()
if sit in 'S':
    resultado = notas(temp,situacao=True)
else:
    resultado = notas(temp)
print(resultado)