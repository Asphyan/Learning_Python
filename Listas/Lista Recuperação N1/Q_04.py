'''
Um programador está criando um jogo de adivinhação,
onde o jogador precisa adivinhar um número secreto entre 1 e 50.
O programa solicita ao jogador que insira um palpite e informa se o palpite é muito alto ou muito baixo.
O jogo continua até que o jogador adivinhe o número correto.
Escreva um programa em Python que implemente esse jogo.
'''

import random

x = random.randrange(1,50)

print('## Jogo do Adivinhe o número ##\n')
print('Digite um número inteiro acerte e ganhe um prêmio!')

while True:
    num = int(input('Digite aqui: '))

    if num < x:
        print('Talvez um pouco maior :/')
    elif num > x:
        print('Talvez um pouco menor :/')
    else:
        print('Parabéns você acertou!!! Aqui, um sorvete pra você <DD.')
        break
