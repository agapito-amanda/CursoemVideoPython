#CLASSIFICANDO ATLETAS; CATEGORIA DE NADADORES 

from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos')

if idade <=9:
    print('Classificação mirim')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')