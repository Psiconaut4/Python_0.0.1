from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto ou 0 para o ano atual '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 !=0 or ano%400 == 0:
    print(f'O ano {ano} é um ano bissexto!')
else: 
    print(f'O ano {ano} não é bissexto!')