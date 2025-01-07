nome = str(input('What is your name? ').capitalize())
if nome == 'Nathan':
    print('Que nome bonito!')
elif nome == 'José' or nome =='Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')

print(f'Tenha um bom dia {nome}')