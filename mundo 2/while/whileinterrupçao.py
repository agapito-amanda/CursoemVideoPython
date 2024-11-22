# INTERROMPENDO REPETIÇÕES ; COMANDO BREAK 

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n 
print(f'a soma vale {s}')