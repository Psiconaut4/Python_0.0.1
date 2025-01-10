print('\033[;31m-=-'*20)
print('Empréstimo Bancário'.center(50))
print('=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\033[m')

valor = float(input('Qual o valor do empréstimo você quer solicitar? R$ '))
print(f'Valor do empréstimo: R${valor}')
salario = float(input('Qual o seu salário mensal? R$ '))
print(f'Salário: R${salario}')
tempo = int(input('Em quantos anos o senhor pretende pagar? '))
print(f'tempo: {tempo}')

prestação = valor / (tempo * 12)
if prestação > salario*(30/100):
    print(f'\033[;31m  Para pagar uma casa de {valor:.2f} em {tempo} anos a prestação será de R${prestação:.2f}. Seu empréstimo foi NEGADO!  \033[m')
else:
    print(f'\033[;32m  Para pagar uma casa de {valor:.2f} em {tempo} anos a prestação será de R${prestação:.2f}. Seu empréstimo foi APROVADO!  \033[m')
