
def ficha(nome='<desconhecido>', gols=0):
    print('--'*20)
    print(f'Nome: {nome}')
    print(f'Gols: {gols}')


n = str(input('Nome: '))
g = str(input('Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g=0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)