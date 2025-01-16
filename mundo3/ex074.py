from random import choices
population = range(0,100)
tupla = (choices(population, k=5))

print(f'lista gerada pelo computador: {tupla}')
print(f'onde o maior número é {max(tupla)} e o menor é {min(tupla)}')