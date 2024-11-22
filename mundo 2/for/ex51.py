# PROGRESSÃO ARITMÉTICA 

primeiro = int(input('primeiro termo: '))
razao = int(input('razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo, razao):
    print(f'{c}', end='- ')
print('FIM!')