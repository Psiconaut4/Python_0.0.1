'''
1 - ler varios números
a) quantos números digitados
b) lista de valores ordenada decrescente
c) se o 5 está ou não na lista.
'''

numeros = []
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    resp = input('Quer continuar? [S/n] ')
    if resp[0] in 'Nn':
        break
if 5 in numeros:
    print('O número 5 está na lista')
if 5 not in numeros:
    print('O número 5 não está na lista.')
numeros.sort(reverse=True)
print(f'você digitou o total de {len(numeros)} numeros')
print(f'Sua lista em ordem decrescente é {numeros}')