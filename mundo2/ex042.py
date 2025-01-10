print('-=-' * 25)
print('Analisador de Triângulos'.center(75, "-"))
print('-=-' * 25)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and b + c > a and c + a > b:
    print('Pode ser um triângulo ', end='')
    if a == b == c:
        print('Equilatero!')
    elif a == b != c or b == c != a or a == c != b:
        print('Isóceles!')
    else:
        print('Escaleno!')
else:
    print('Não pode ser um triângulo.')
