# TRATANDO VÁRIOS VALORES V1

# no caso abaixo eu estou apenas resumindo as variáveis, já que elas recebem o mesmo valor

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre elas foi {soma}!')