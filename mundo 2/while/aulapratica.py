# r = 'S'

# while r =='S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N]')).upper()
# print('FIM')

n = 1 
impar = par = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n !=0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print(f'Vc digitou {par} números pares e {impar} números ímpares ')