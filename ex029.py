print('-' * 50)
print('RADAR DE VELOCIDADE'.center(50))
print('-' * 50)

vel = float(input('Digite a sua velocidade: '))
if vel >= 80:
    multa = (vel - 80) * 7
    print(f'MULTADO! você excedeu o limite de velocidade de 80km/h, sua multa é de R${multa:.2f}.')
print('Tenha um bom dia, Dirija com segurança!')