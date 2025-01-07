from random import randint
from time import sleep
print('-=-'*35)
print('Olá jogador bem-vindo(a) ao game, vou gerar um número aleatório de 0 a 3 e você terá que adivinhar.')
print('-=-'*35)
yes = str(input('Você está pronto? S/N ').upper())
if yes == 'S':
    print('PROCESSANDO...')
    sleep(2)
    num = randint(0, 3)
    jogador = int(input('Pensei em um número de 0 a 3, tente adivinhar: '))
    if jogador == num:
        print(f'PARABÉNS! eu pensei no número {num}, você conseguiu me vencer.')
    else:
        print(f'Vish.. eu pensei em {num} Você perdeu! GAME OVER.')
else:
    print('Jogo Encerrado.')