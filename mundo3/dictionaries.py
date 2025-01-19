'''pessoas = {'nome': 'Nathan', 'sexo': 'M', 'idade': 24}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.values())
print(pessoas.keys())
print(pessoas)
print(pessoas.items())
pessoas['peso'] = 70
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
brasil.append(estado)
brasil.append(estado2)

print(brasil[1]['uf'])
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()