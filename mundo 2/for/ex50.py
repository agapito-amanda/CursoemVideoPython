soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'voce informou {cont} numeros PARES e a soma foi {soma}')