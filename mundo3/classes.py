class Vendedor:
    def __init__(self, nome, vendas, meta):
        self.nome = nome
        self.vendas = vendas
        if self.vendas >= meta:
            print(f'{self.nome} Bateu a meta!')
        else:
            print(f'{self.nome} Não bateu a meta!')

