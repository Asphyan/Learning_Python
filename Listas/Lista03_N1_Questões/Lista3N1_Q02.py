'''
Escreva um programa que leia uma string 
e use uma pilha para inverter a ordem das palavras.
'''

from Classic_Stack import Pilha

def inverter_ordem_palavras(frase):
    palavras = frase.split()
    pilha = Pilha()
    resultado = []

    for palavra in palavras:
        pilha.push(palavra)

    while not pilha.is_empty():
        resultado.append(pilha.pop())

    return ' '.join(resultado)

frase = input("Digite uma frase: ")
frase_invertida = inverter_ordem_palavras(frase)
print("Frase invertida:", frase_invertida)
