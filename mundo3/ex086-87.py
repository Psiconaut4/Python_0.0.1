'''criar matriz 3x3 e preencher com valores lidos pelo teclado
mostrar matriz na tela com formatação correta

mostrar a soma dos valores pares
a soma dos valores da terceira coluna
o maior valor da segunda linha'''
linha1 = []
linha2 = []
linha3 = []
matrix = []
somapar = 0
somacoluna = 0
for c in range(0, 3):
    linha1.append(int(input(f'Digite um valor para [0, {c}]: ')))
matrix.append(linha1)
for c in range(0, 3):
    linha2.append(int(input(f'Digite um valor para [1, {c}]: ')))
matrix.append(linha2)
for c in range(0, 3):
    linha3.append(int(input(f'Digite um valor para [2, {c}]: ')))
matrix.append(linha3)
print('-=-'*20)
for i, l in enumerate(matrix):
    for p, v in enumerate(l):
        if v % 2 == 0:
            somapar += v
    if p == 2:
        somacoluna += v
print(somapar)
print(somacoluna)