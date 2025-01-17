numeros = []
while True:
    num = input('Digite um número para adiciona-lo a lista: ')
    if num not in numeros:
        numeros.append(num)
    else:
        print('Valor duplicado, não adicionado.')
    resp = input('Quer continuar [S/n]: ')
    if resp in 'Nn':
        break
numeros.sort()
print(f'{numeros}')