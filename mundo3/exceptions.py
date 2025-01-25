try:
    1/0
except Exception as erro:
    print(f'Nome do erro: {erro}')
finally:
    print('Arruma essa bagaça')