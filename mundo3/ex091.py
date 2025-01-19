'''
quatro jogadores jogam dado e tenham resultados aleatórios, guardar em um dicionário. no final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

pessoas = []
for c in range(0, 4):
    jogador = {'nome': '', 'jogada': ''}
    jogador['nome'] = str(input('Nome do Jogador: '))
    a = randint(0, 6)
    jogador['jogada'] = a
    pessoas.append(jogador)

for c, v in enumerate(pessoas):
    if c == 0:
        win = pessoas[c]['nome']
    if c <= len(pessoas) and pessoas[c]['jogada'] > pessoas[c-1]['jogada']:
        win = pessoas[c]['nome']
    sleep(1)
    print(f'o dado para o jogador {pessoas[c]["nome"]} caiu em {pessoas[c]["jogada"]}')
print('-=-'*20)
print(f'o {win} venceu.')