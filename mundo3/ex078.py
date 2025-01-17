menor = 999
maior = 0
valores = []
for num in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if valores[num] < menor:
        menor = valores[num]
    elif valores[num] > maior:
        maior = valores[num]

print(f'você criou a lista {valores} \n {maior} foi o maior valor encontrado \n {menor} foi o menor valor encontrado.')