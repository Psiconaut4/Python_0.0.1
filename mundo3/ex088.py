'''programa para ajudar jogar na MEGASENA perguntar quantos jogos serão gerados e sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta'''
from random import sample

print('-=-'*20)
print(f'{' JOGOS MEGA-SENA ':~^60}')
print('-=-'*20)
jogos = (int(input('Quantos jogos você quer gerar?: ')))
print('_'*60)

sorteio = list()
for c in range(0, jogos):
    sorteio.append(sample(range(1, 61), 6))
for u in sorteio:
    print(u)