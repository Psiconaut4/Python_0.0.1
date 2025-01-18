"""
ler 7 valores numéricos e cadastrar em uma lista que separe os pares dos impares
mostrar os valores pares e impares em ordem crescente
"""
lista = list()
pares = list()
impares = list()
for c in range(0,7):
    lista.append(int(input(f'Digite o {c+1}o. valor: ')))
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
pares.sort()
impares.sort()
lista.clear()
lista.append(pares)
lista.append(impares)
print(f'Os valores pares digitados foram: {pares}\nOs valores ímpares digitados foram {impares}')