'''def soma(a, b=2):
    print(f'a = {a}, b = {b}')
    s = a + b
    print(f'A + B = {s}')


soma(3,3)
'''
'''def contador(* num):
    tam = len(num)
    print(f'{tam} valores ao todo')


contador(2, 1, 7)
contador(1, 2)
contador(7, 7)'''

valores = [2, 5, 7, 4, 2, 9]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

print(valores)
dobra(valores)