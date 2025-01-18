'''criar matriz 3x3 e preencher com valores lidos pelo teclado
mostrar matriz na tela com formatação correta

mostrar a soma dos valores pares
a soma dos valores da terceira coluna
o maior valor da segunda linha'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

    '''for p, v in enumerate(l):
        if v % 2 == 0:
            somapar += v
    if p == 2:
        somacoluna += v
'''