nome = input('Digite seu nome completo: ')
print(f'Seja bem-vindo(a) {nome}.')
print(f'Seu nome em letras maiúsculas é: {nome.upper()}')
print(f'Em letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(''.join(nome.split()))} letras ao todo!')
pn = nome.split()
print(f'Seu primeiro nome tem {len(pn[0])} letras!')