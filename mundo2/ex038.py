while True:
    try:
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))

        if numero1 > numero2:
            print(f'O primeiro valor {numero1} é o maior!')
        elif numero2 > numero1:
            print(f'O segundo valor {numero2} é o maior')
        elif numero1 == numero2:
            print(f'Não existe maior, o primeiro valor {numero1} e o segundo valor {numero2} são iguais!')
        else:
            print('Opção inválida. Tente novamente.')
        
        escolha = input('Deseja ir de novo? [S/n]: ').lower()
        if escolha == 'n':
            print('Até logo!')
            break
    except ValueError:
        print('Por favor, Insira um número inteiro válido.')