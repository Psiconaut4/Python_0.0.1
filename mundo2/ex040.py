print('A seguir digite suas últimas 3 notas para calcular a média:')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 5.0:
    print(f'Sua média é {media}. Você foi reprovado!')
elif media > 5.0 and media < 6.9:
    print(f'Sua média é {media}. Você está de recuperação!')
else:
    print(f'Sua média é {media}. Aprovado!')