#ÍNDICE DE MASSA CORPORAL 

altura = float(input('Qual sua altura? (m) '))
peso = float(input('Quanto você pesa? (Kg) '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO normal. \nSeu IMC é {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'Você está na faixa de PESO NORMAL. \nSeu IMC é {imc:.1f}')
elif 25 <= imc < 30:
    print(f'Você está em SOBREPESO. \nSeu IMC é {imc:.1f}')
elif 30 <= imc < 40:
    print(f'Você está em OBESIDADE. \nSeu IMC é {imc:.1f}')
elif imc >= 40:
    print(f'Você está em OBESIDADE MÓRBIDA. \nSeu IMC é {imc:.1f}')



