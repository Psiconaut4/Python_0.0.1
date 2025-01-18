from random import sample

print('-=-'*20)
print(f'{' JOGOS MEGA-SENA ':~^60}')
print('-=-'*20)
jogos = (int(input('Quantos jogos você quer gerar?: ')))
print('_'*60)

sorteio = list()
for c in range(0, jogos):
    sorteio.append(sample(range(1, 61), 6))
print('-=' * 3, f' SOTEANDO {jogos} JOGOS ', '-=' * 3)
for c in range(0, jogos):
    print(f'Jogo {c+1}:  {sorteio[c]}')
print('>>>>>>>>>> Volte Sempre <<<<<<<<<<')