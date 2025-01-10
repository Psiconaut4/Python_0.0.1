from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = (date.today().year - ano)
if idade == 18:
    print('Chegou a hora de se alistar garotão!')
elif idade < 18:
    falta = 18 - idade
    print(f'Calma jovem, inda faltam {falta} anos para você se alistar!')
elif idade > 18:
    atraso = idade - 18
    print(f'Já passou sua hora de se alistar, está atrasado em {atraso} anos.')