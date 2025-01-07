distancia = float(input('Qual a distância da viagem? '))
if distancia <= 200:
    print(f'O preço da sua passagem foi R${distancia*0.5:.2f}')
elif distancia > 200:
    print(f'O preço da passagem foi R${distancia*0.45}')