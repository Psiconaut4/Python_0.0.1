#verificar se a primeira palavra é "santo"

cid = input('digite o nome de uma cidade: ').strip()
print(cid[:5].upper() == 'SANTO')