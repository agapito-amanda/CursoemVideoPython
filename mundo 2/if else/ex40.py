#CALCULANDO MÉDIA DO ALUNO
nota1 = float(input('digite a nota do primeiro bimestre: '))
nota2 = float(input('digite a nota do seu segundo bimestre: '))
media = (nota1 + nota2)/2
print(f'Tirando {(nota1):.1f} e {(nota2):.1f}, a média  é {(media):.1f}')

#lê-se 'a média é maior ou igual a 5, só que a média é menor do que 7' OBS.: "7 > media" o sete ta maior que a média
if 7 > media >= 5:
    print('O aluno está em recuperação.')

elif media < 5:
    print('O aluno está reprovado.')

#Poderia ter colocado else aqui embaixo, mas dessa forma ajuda na legibilidade do script. Lembre-se que outros programadores também podem ver seu código, então ele precisa ser claro

elif media >= 7:
    print('O aluno está aprovado.')




#MÉTODO TRADICIONAL
'''if media < 5.0:
    print(f'Sua média foi: {media}. \nVocê está reprovado!')
elif media == 5.0 and 6.9:
    print(f'Sua média foi: {media}. \nVocê está de recuperação!')
else: 
    print(f'Sua média foi: {media}. \nVocê está aprovado!')'''