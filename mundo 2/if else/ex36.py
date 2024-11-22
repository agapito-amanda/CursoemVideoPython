#FINANCIAMENTO E EMPRÉSTIMO

casa = float(input('Valor da casa? '))
salario = float(input('Qual salário do comprador? '))
valor_anual = int(input('Quantos anos de financiamento? '))
prestacao = casa/(valor_anual * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {valor_anual} anos, \na prestação será de R${prestacao:.2f}')

#print(f'COMPARANDO {prestacao:.2f} com o {minimo}')

if prestacao <= minimo:
    print('O empréstimo foi CONCEDIDO!')
else:
    print('O empréstimo foi NEGADO!')