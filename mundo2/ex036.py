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
    print('\033[;31mSeu empréstimo foi negado!\033[m')
else:
    print('\033[;32mSeu empréstimo foi aprovado!\033[m')
