cont = 0
tabuada = int(input('digite um valor para fazer a tabuada (negativo para sair): '))
while True:
    if tabuada < 0:
        break
    for cont in range(11):
        print(f'{tabuada} X {cont} = {tabuada * cont}')
        cont = cont + 1
    print('~~'*20)
    tabuada = int(input('digite um valor para fazer a tabuada: '))
    print('~~'*20)
print('Fim do Programa')