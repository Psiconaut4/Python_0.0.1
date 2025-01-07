sal = float(input('Digite o salário do funcionário: '))
if sal >= 1250:
    novosal = sal + sal * (10/100)
    print(f'com o reajuste de 10 por cento seu novo salário é de R${novosal:.2f}')
elif sal <= 1250:
    novosal = sal + sal * (15/100)
    print(f'com o reajuste de 15 por cento seu novo salário é de R${novosal:.2f}')