'''
ler varios números
a) criar duas listas uma com os pares e outra os impares
b) mostrar conteúdo das 3 listas geradas
'''
numeros = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar? [S/n]: '))
    if resp in 'Nn':
        break
print(f'A lista que você criou: {numeros}')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')