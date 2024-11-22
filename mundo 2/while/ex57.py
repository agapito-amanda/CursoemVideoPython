# LIMITANDO A DIGITAÇÃO SEXO F OU M

sexo = str(input('Difite seu sexo: [F/M]')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('OPção inválida. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')