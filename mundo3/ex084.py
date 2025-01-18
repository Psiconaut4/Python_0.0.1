'''
ler nome e peso de varias pessoas

quantas pessoas foram cadastradas
uma listagem com as pessoas mais pesadas
uma lista com as pessoas mais leves'''
dado = []
pessoas = []
pesado = []
leve = []
total = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    total += 1
    resp = str(input('Quer continuar? [S/n]: '))
    if resp in 'Nn':
        break
for p in pessoas:
    if p[1] >= 100:
        pesado.append(p)
    elif p[1] <= 50:
        leve.append(p)
print(f'Ao todo foram cadastradas {total} pessoas.')
print(f'as pessoas mais pesadas foram {pesado}.')
print(f'E as mais leves foram {leve}.')