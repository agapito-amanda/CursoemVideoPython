# SEQUENCIA  DE FIBONACCI V1 (SOMA DOIS TERMOS ANTERIORES)

print('-'*30)
print('Sequencia de Fiboonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} -- {t2}', end=' ')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f'-- {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1 
print('- FIM!')