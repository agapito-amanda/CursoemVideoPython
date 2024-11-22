#GERENCIADOR DE PAGAMENTOS

print('{:=^40}'.format(' BOUTIQUE AGAPITOS '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO: 
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual forma de pagamento? '))

if opcao ==1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${(parcela):.2f} SEM JUROS')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_parcela
    print(f'Sua compra será parcelada em {total_parcela}x de {(parcela):.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO DE PAGAMENTO INVÁLIDA. TENTE NOVAMENTE.')

print(f'Sua compra de R${(preco):.2f} vai sair por R${(total):.2f} no final.')

