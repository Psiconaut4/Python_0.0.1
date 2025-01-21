from random import randint
from time import sleep
from operator import itemgetter

jogo = {input('Nome: '): randint(1, 6),
        input('Nome: '): randint(1, 6),
        input('Nome: '): randint(1, 6),
        input('Nome: '): randint(1, 6)}
ranking = []
print('__'*20)
for k, v in jogo.items():
    print(f'{f"{k} tirou {v} no dado.":^40}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('--'*20)
print(f'{"== RANKING DOS JOGADORES ==":^40}')
print('__'*20)
for i, v in enumerate(ranking):
    print(f'{f"{i+1}º lugar: {v[0]} com {v[1]}.":^40}')
    sleep(0.5)
'''
for c in range(0, 4):
    jogador = {'nome': '', 'jogada': ''}
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['jogada'] = int(randint(1, 6))
    pessoas = jogador
ranking = {}
ranking = sorted(pessoas.items(), key=itemgetter(3))
for 'nome', 'jogada' in pessoas.items():
    print(f'o {"nome"} tirou {"jogada"} no dado.')
print(ranking)'''


'''for c, v in enumerate(pessoas):
if c == 0:
    ranking['1lugar'] = pessoas[c]
elif c <= len(pessoas) and pessoas[c]['jogada'] > pessoas[c-1]['jogada']:
    ranking['1lugar'] = pessoas[c]
elif pessoas[c]['jogada'] < ranking['1lugar']['jogada'] and pessoas[c]['jogada'] > pessoas[c-1]['jogada']:
    ranking['2lugar'] = pessoas[c]
elif pessoas[c]['jogada'] < pessoas[c-1]['jogada']:
    ranking['3lugar'] = pessoas[c]
else:
    ranking['4lugar'] = pessoas[c]
'''

'''print(f'o dado para o jogador {pessoas[c]["nome"]} caiu em {pessoas[c]["jogada"]}')
print('-=-'*20)
sleep(1)
for c, v in enumerate(pessoas):
    print(pessoas[c])'''