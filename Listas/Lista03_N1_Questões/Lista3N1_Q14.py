'''
Escreva um programa que leia uma expressão matemática na forma de string 
e utilize uma pilha para converter a expressão para a notação polonesa reversa.
'''

from Classic_Stack import Pilha

def polonesa_reversa(expressao):

    pilha = Pilha()
    polonesa_reversa = ''
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for caracter in expressao:
        if caracter.isnumeric():
            polonesa_reversa += caracter
        elif caracter == '(':
            pilha.push(caracter)
        elif caracter == ')':
            topo = pilha.pop()
            while topo != '(':
                polonesa_reversa += topo
                topo = pilha.pop()
        else:
            while not pilha.is_empty() and precedencia[caracter] <= precedencia.get(pilha.top(), 0):
                polonesa_reversa += pilha.pop()
            pilha.push(caracter)

    while not pilha.is_empty():
        polonesa_reversa += pilha.pop()

    return polonesa_reversa

expressao = input("Digite a expressão: ")
polonesa_reversa = polonesa_reversa(expressao)

print("Polonesa Reversa:", polonesa_reversa)
