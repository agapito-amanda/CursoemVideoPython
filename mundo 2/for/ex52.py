#NUMEROS PRIMOS

num = int(input('digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ') #esse código no contra barra é de cor
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[31mO numero {num} foi divisível {tot} vezes')
if tot == 2:
    print('e por isso ele é PRIMO!')
else:
    print('por isso  ele NÃO É PRIMO')
