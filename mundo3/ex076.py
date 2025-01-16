listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Tênis', 400.00,
            'Caderno', 20.00,
            'Linguiça', 100,
            'Frango', 50.00,
            'Buceta', 00.0,
            'Ai caraho', 6669.69)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
