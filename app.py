import random
# import math

# número = float(input('Digite um número real qualquer: '))
# print(f'O número {número} tem a parte inteira {math.floor(número)}')

# co = float(input('Dê o valor do cateto oposto: '))
# ca = float(input('Dê o valor do cateto adjacente: '))
# print(f'conforme os valores dos catetos é correto afirmar que o comprimento da hipotenusa é: {math.hypot(co,ca)} ')

# grau = math.radians(int(input('Dê o valor do ângulo em graus: ')))

# seno = math.sin(grau)
# cosseno = math.cos(grau)
# tangente = math.tan(grau)

# print(f'Dado o ângulo é correto afirmar que:\n o Seno do ângulo é: {seno:.3f} \n o Cosseno: {cosseno:.3f} \n e a Tangente: {tangente:.3f} ')

lista = []
while True:
    aluno = input(
        'Digite o nome do aluno para sortear um (ou "encerrar" para finalizar): ')

    if aluno.lower() == 'encerrar':
        break
    lista.append(aluno)

sorteio = random.sample(lista, 3)
print(f'Os alunos sorteados foram: {sorteio}')
