numeros = []
while True:
    num = input('Digite um número para adiciona-lo a lista: ')
    if num in numeros:
        print('Valor duplicado, não adicionado.')
        numeros.remove(num)
    numeros.append(num)
    resp = input('Quer continuar [S/n]: ')
    if resp[0] in 'Nn':
        break
numeros.sort()
print(f'{numeros}')