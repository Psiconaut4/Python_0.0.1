from random import choice
from time import sleep
# Banner Principal
print('-=-'*25)
print('Jo Ken Pô'.center(75))
print('-=-'*25)
while True:
    try:
        # Escolha do PC
        jokenpo = ('Pedra', 'Papel', 'Tesoura')
        pc = choice(jokenpo)
        print('''Suas opções:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')

        # Escolha do player
        player = int(input('Pedra, Papel ou Tesoura? '))
        print('JO'.center(25))
        sleep(1)
        print('KEN'.center(27))
        sleep(1)
        print('PO'.center(25))

        # Resultado do Jogo
        print('=-='*25)
        print(f'Jogador jogou {jokenpo[player]}')
        print(f'Computador jogou {pc}')
        print('=-='*25)

        if (pc == 'Pedra' and player == 2) or (pc == 'Papel' and player == 0) or (pc == 'Tesoura' and player == 1):
            print('Se fudeu, Game Over')
        elif (player == 0 and pc == 'Tesoura') or (player == 1 and pc == 'Pedra') or (player == 2 and pc == 'Papel'):
            print('Parabéns! Você Ganhou!')
        else:
            print('Cagada ein, Empate!')
        
        # Pergunta se o jogador quer continuar
        resposta = input('Jogar novamente? [S/n]: '.lower())
        if resposta == 'n':
            print('Foi bom jogar com você!')
            break
    except Exception as e:
        print(f'Error 404. Comando {e} inválido.')
