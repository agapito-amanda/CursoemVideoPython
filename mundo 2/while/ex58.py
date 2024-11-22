#JOGO DE ADIVINHAÇÃO

from random import randint
computador = randint(0, 10)

print('Olá, caro user. Sou Frajola, seu computador, e acabei de pensar em um número entre 0 e 10.')
print('Será que consegue acertar qual foi?')
acertou = False 
palpites = 0

'''use o while not quando vc for fzr um script que nem sempre vamos saber qual escolha do usuário. dá-se que é falso enquanto não inserir um valor verdadeiro'''

while not acertou:    
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
print(f'Acertou com {palpites} tentativas. Parabéns!')