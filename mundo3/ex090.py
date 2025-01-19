'''
nome e média de um aluno
e a situação
depois mostrar na tela
'''
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Qual a média do aluno?: '))
if aluno['média'] <= 6.0:
    print(f'O aluno {aluno["nome"]} com média {aluno["média"]} está reprovado. ')
else:
    print(f'O aluno {aluno["nome"]} com média {aluno["média"]} está aprovado! ')