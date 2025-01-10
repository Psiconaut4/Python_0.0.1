print('-=-' * 25)
print('Analisador de Triângulos'.center(75, "-"))
print('-=-' * 25)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('Pode ser um triângulo!')
else:
    print('Não pode ser um triângulo.')
