#CRIANDO MENU DE OPÇÕES 
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''
    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR  
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA
    ''')
    opcao = int(input('>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')

    elif opcao == 2: 
        produto = n1 * n2 
        print(f'O resultado de {n1} e {2} é {produto}')

    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')

    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))    
        n2 = int(input('Segundo valor: '))    

    elif opcao == 5:
        print('Finalizando...')

    else: 
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa!')