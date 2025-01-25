def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! 404 PAGE NOT FOUND \033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')