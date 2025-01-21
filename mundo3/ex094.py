dado = {}
cadastro = []
mulheres = []
media = 0
while True:
    dado['nome'] = str(input('Nome: '))
    dado['sexo'] = str(input('Sexo: [M/F] ').upper())
    while dado['sexo'][0] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F')
        dado['sexo'] = str(input('Sexo: [M/F] ').upper())
    if dado['sexo'] == 'F':
        mulheres.append(dado['nome'])
    dado['idade'] = int(input('Idade: '))
    media += dado['idade']
    cadastro.append(dado.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    while resp not in 'SN':
        print('ERRO! Por favor, digite apenas S ou N')
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = media / len(cadastro)
print(f'B) A média de idade é de {media:.1f} anos.')

if len(mulheres) > 0:
    print(f'C) as mulheres cadastradas foram: ', end='')
    for v in mulheres:
        print(f'{v} |', end=' ')
    print()
else:
    print('C) Nenhuma mulher foi cadastrada.')

print('D) Lista das pessoas que estão acima da média: ')
print('__'*30)
for p in cadastro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')