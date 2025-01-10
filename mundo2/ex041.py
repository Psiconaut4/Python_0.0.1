from datetime import date
ano = int(input('Digite seu ano de Nascimento: '))
idade = date.today().year - ano
if idade < 9:
    print('Categoria mirim.')
elif idade > 9 and idade <= 14:
    print('Categoria infantil.')
elif idade > 14 and idade <= 19:
    print('Categoria Júnior.')
elif idade > 19 and idade <= 20:
    print('Categoria Sênior.')
else:
    print('Categoria Master.')