#ANO DE ALISTAMENTO
from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}!')

if idade == 18:
    print('Você já tem 18 anos, é hora de se alistar!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem idade pra se alistar! Ainda faltam {saldo} anos para alistamento')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos!')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')