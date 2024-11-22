#COMPARANDO PESOS

menor = 0
maior = 0

for pessoas in range(1, 6):
    peso = float(input(f'Peso da {pessoas}a pessoa: '))
    if pessoas == 1:
        maior = peso 
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi {maior}Kg e o menor foi {menor}Kg')
