print('='*30)
print('{:^30}'.format('SINTECH BOLADONA'))
print('='*30)

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'cédulas de R${céd:.2f}: {totcéd}')
        if céd == 50:
            céd = 20
            totcéd = 0
        elif céd == 20:
            céd = 10
            totcéd = 0
        elif céd == 10:
            céd = 1
            totcéd = 0
        if total == 0:
            break