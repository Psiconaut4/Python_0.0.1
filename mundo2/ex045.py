import random
# Banner Principal
print('-=-'*25)
print('JoKenPô'.center(75))
print('=-='*25)
while True:
    try:
        # Escolha do PC
        jokenpo = ['Pedra', 'Papel', 'Tesoura']
        
        pc = random.choice(jokenpo)

        # Escolha do player
        player = str(input('Pedra, Papel ou Tesoura? ')).title()

        # Verifica se a entrada do player é válida
        if player not in jokenpo:
            print("Escolha inválida! Tente novamente.")
            continue

        # Resultado do Jogo
        print('=-='*25)
        print(f'você: {player} X computador: {pc}'.center(50))
        print('=-='*25)
        if (pc == 'Pedra' and player == 'Tesoura') or (pc == 'Papel' and player == 'Pedra') or (pc == 'Tesoura' and player == 'Papel'):
            print('Se fudeu, Game Over')
        elif (player == 'Pedra' and pc == 'Tesoura') or (player == 'Papel' and pc == 'Pedra') or (player == 'Tesoura' and pc == 'Papel'):
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
