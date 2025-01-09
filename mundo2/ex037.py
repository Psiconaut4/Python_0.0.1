while True: 
    try:
        dec = int(input('Qual o número inteiro você quer converter? '))
        escolha = input('''
            Digite [2] para Binário
            Digite [8] para Octal
            Digite [16] para HexaDecimal
                ou sair para encerrar
        ''')
        #seletor do tipo de conversor:
        if escolha == '2':
            print(f'{bin(dec)[2:]}')
        elif escolha == '8':
            print(f'{oct(dec)[2:]}')
        elif escolha == '16':
            print(f'{hex(dec)[2:]}')
        elif escolha.lower() == 'sair':
            print('Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')

        volta = input('Deseja voltar? [S/n]').lower()
        if volta == 'n':
            print('Até logo!')
            break
    except ValueError:
            print('Por favor, insira um número inteiro válido.')