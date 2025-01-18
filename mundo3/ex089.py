cadastros = []
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
print('-=-'*60)
print('No. NOME                MÉDIA')
print('--'*20)
