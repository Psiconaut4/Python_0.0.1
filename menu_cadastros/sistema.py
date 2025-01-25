from libs.interface import *


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        cabeçalho('Opção 1')
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('\033[32mSaindo do sistema... até logo!\033[m')
        break
    else:
        print('Digite uma opção válida!')