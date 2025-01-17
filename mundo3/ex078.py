menor = 999
maior = 0
valores = []
posmaior = []
posmenor = []
for pos in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if valores[pos] < menor:
        menor = valores[pos]
    elif valores[pos] > maior:
        maior = valores[pos]
for p, numero in enumerate(valores):
    if numero == maior:
        posmaior.append(p)
    elif numero == menor:
        posmenor.append(p)
print(f'você criou a lista {valores} \n {maior} foi o maior valor encontrado nas posições {posmaior} \n {menor} foi o menor valor encontrado nas posições {posmenor}.')