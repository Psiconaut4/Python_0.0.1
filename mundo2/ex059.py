from time import sleep
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

escolha = 0
while escolha != 5:
    print("""
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÙMEROS
    [ 5 ] SAIR DO PROGRAMA
    """)
    escolha = int(input('Escolha um número: '))
    if escolha == 1:
        print(f'A soma de {a} e {b} é {a+b}.')
    elif escolha == 2:
        print(f'{a} X {b} = {a*b}')
    elif escolha == 3:
        if a > b:
            print(f'{a} é maior que {b}')
        else:
            print(f'{b} é maior que {a}')
    elif escolha == 4:
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
    elif escolha == 5:
        break
    else:
        print('opção inválida!')
    print('-=-'*10)
    sleep(2)
print('Fim do Programa!')
