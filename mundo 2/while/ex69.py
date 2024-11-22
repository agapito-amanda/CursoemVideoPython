# ANÁLISE DE DADOS DO GRUPO

tot18 = totH = totM20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo  == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas +18 anos: {tot18}')
print(f'Ao total, temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulheres com MENOS de 20 anos')