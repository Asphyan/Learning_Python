'''
Escreva um programa que leia uma string contendo caracteres (, ), {, }, [ e ], 
e use uma pilha para verificar se os caracteres estão balanceados.
'''
from Classic_Stack import Pilha

def verificar_balanceamento(expressao):
    pilha = Pilha()

    for caracter in expressao:
        if caracter in '([{':
            pilha.push(caracter)
        elif caracter in ')]}':
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (caracter == ')' and topo != '(') or \
                    (caracter == ']' and topo != '[') or \
                    (caracter == '}' and topo != '{'):
                return False

    return pilha.is_empty()

expressao = input('Digite uma expressão (), {}, []: ')

if verificar_balanceamento(expressao):
    print('Estão balanceados.')
else:
    print('Não estão balanceados.')
