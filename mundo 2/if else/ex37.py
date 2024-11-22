#CONVERSOR DE DADOS 

num = int(input('Informe um número inteiro: '))
print(''' Escolha a base para converter: 
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Sua opção:'))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a: {(bin(num) [2:])}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a: {(oct(num) [2:])}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a: {(hex(num)[2:])} ')
else:
    print('Opção inválida. Tente novamente.')