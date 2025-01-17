'''usuario1 = []
usuario1.append('Nathan')
usuario1.append(24)
user2 = []
user2.append('Julia')
user2.append(19)
usuarios = []
usuarios.append(usuario1)
usuarios.append(user2[:])
user2[0] = 'Maria'
user2[1] = 24
usuarios.append(user2[:])
print(usuarios)'''

galera = list()
dado = []
totmai = totmenor = 0
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Da galera listada {totmai} são maiores de idade e {totmenor} são menores de idade')

'''lista = list()
data = list()
for c in range(0, 2):
    data.append(str(input('Nome: ')))
    data.append(int(input('Idade: ')))
    lista.append(data[:])
    data.clear()  
print(lista)
print(data)'''