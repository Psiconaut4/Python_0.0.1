from libs.interface import *
from libs.arquivo import *

arq = 'menu_cadastros/cadastros.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar conteúdo do arquivo
        lerArquivo(arq)
    elif resp == 2:
        cabeçalho('Opção 2')
    elif resp == 3:
        cabeçalho('\033[32mSaindo do sistema... até logo!\033[m')
        break
    else:
        print('\033[31mDigite uma opção válida!\033[m')