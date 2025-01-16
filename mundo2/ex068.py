from random import randint
jogador = str(input('''
[ 0 ] Para PAR
[ 1 ] Para ÍMPAR
\n'''))
vitoria = 0
while True:
    if jogador not in '01':
        print('Escolha inválida!')
        break
    pc = randint(0,5)
    jogada = int(input('Digite um número de 1 a 5: '))
    if jogador == '0':
        if (jogada + pc) % 2 == 0:
            print(f'Você: {jogada} + {pc}: Computador = Par, você ganhou!')
            vitoria = vitoria + 1
        elif (jogada + pc) % 2 == 1:
            print(f'Você: {jogada} + {pc}: Computador = Ímpar, você perdeu!')
            break
    if jogador == '1':
        if (jogada + pc) % 2 == 1:
            print(f'Você: {jogada} + {pc}: Computador = Ímpar, você ganhou!')
            vitoria = vitoria + 1
        elif (jogada + pc) % 2 == 0:
            print(f'Você: {jogada} + {pc}: Computador = Par, você perdeu!')
            break

print(f'Você ganhou {vitoria} vezes, parabéns')