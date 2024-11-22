# VÁRIOS NÚMEROS COM FLAG 

n = n_digitado = s = 0

while True:
    n = int(input('digite um número (99 para  parar): '))
    if n == 999:
        break
    n_digitado += 1
    s += n
print(f'Foram {n_digitado} números digitados e a soma entre eles resultou em {s}')
