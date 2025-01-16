tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número de 1 a 20 para ler ele por extenso: '))
while num not in range(0, 21):
    num = int(input('Valor inválido, Digite novamente um número de 0 a 20: '))
print(f'você digitou o número {tupla[num]}.')