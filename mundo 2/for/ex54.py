#ANÁLISE DE IDADES 
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoas}a nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Tivemos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade!')