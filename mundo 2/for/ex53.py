#PALÍNDROMO 

# JEITO TRADICIONAL
'''frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso +=junto[letra]

print(f'o inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palindromo')
else:
    print('NÃO É palindromo')'''

# USANDO FATIAMENTO 

frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'o inverso de {junto} é {inverso}')

if inverso == junto:
    print('É um palíndromo')
else:
    print('NÃO É palíndromo')