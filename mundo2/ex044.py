print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção de pagamento? '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra de R${preço:.2f}, será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')
print(f'Sua compra de R${preço:.2f} vai custar {total:.2f} no final.')