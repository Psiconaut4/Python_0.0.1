#peso/(altura x altura)

print('Calculadora de IMC')
peso = float(input('Primeiro digite seu peso(Kg): '))
altura = float(input('Agora digite a sua Altura(Mts): '))
imc = peso / (altura * altura)
print(f'Dados peso e altura, podemos afirmar que seu IMC (índice de massa corporal) é de: {imc}')