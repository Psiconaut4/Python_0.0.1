'''cadastros = []
perfil = []
dado = []
while True:
    perfil.append(input('Nome: ').capitalize())
    dado.append(float(input('Nota 1: ')))
    dado.append(float(input('Nota 2: ')))
    perfil.append(dado[:])
    cadastros.append(perfil[:])
    dado.clear()
    perfil.clear()
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('-=-'*20)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>10}')
print('--'*20)
'''

cadastros = list()
while True:
    nome = str(input('Nome: ').capitalize())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    cadastros.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/n]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>10}')
print('-'*30)
for i, a in enumerate(cadastros):
    print(f'{i:<4}{a[0]:<10}{a[2]:>9.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(cadastros) - 1:
        print(f'Notas de {cadastros[opc][0]} são {cadastros[opc][1]}.')