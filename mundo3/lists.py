'''valores = list(range(1,21))
del valores[5:15]
valores.append(5)
valores.insert(1,5)
valores.pop(1)
while 5 in valores:
    valores.remove(5)
print(valores)
valores.sort(reverse=True)
print(valores)
for p, v in enumerate(valores):
    print(f'na posição {p} encontrei o valor {v}')
print('final da lista')'''

a = list(range(0,9,2))
b = a[:]
b[2] = 5
print(a)
print(b)