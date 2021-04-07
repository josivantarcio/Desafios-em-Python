aluno = {}
aluno['nome'] = str(input('Digite o nome: ')).strip().title()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
for k, v in aluno.items():
    print(f"{k} - {v}")