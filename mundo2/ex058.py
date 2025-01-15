from random import randint
from time import sleep
print('-=-'*35)
print('Olá jogador bem-vindo(a) ao game, vou gerar um número aleatório de 0 a 5 e você terá que adivinhar.')
print('-=-'*35)
yes = str(input('Você está pronto? S/N ').upper())
if yes == 'S':
    print('PROCESSANDO...')
    sleep(2)
    num = randint(0, 5)
    palpite = 1
    jogador = int(input('Pensei em um número de 0 a 5, tente adivinhar: '))
    while jogador != num:
        jogador = int(input('Tente novamente: '))
        palpite += 1
    if jogador == num:
        print(f'PARABÉNS! eu pensei no número {num}, você conseguiu me vencer e só levou {palpite} palpites.')
else:
    print('Jogo Encerrado.')