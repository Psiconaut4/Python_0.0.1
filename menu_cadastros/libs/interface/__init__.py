from time import sleep


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    sleep(1)
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    print('-'*42)
    print('{:^42}'.format('MENU PRINCIPAL'))
    print('-'*42)
    sleep(1)
    c = 1
    for item in lista:
        print(f'\033[;33m{c} -\033[m \033[;34m{item}\033[m')
        c += 1
    print('-'*30)
    sleep(0.5)
    r = leiaInt('\033[;34mSua Opção: \033[m')
    return r
