tupla = (int(input('Digite o primeiro valor: ')),
         int(input('Digite o Segundo: ')),
         int(input('Digite o Terceiro: ')),
         int(input('Digite o Quarto: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'o número 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print('Valor 3 não digitado.')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')