'''
Escreva um programa que use uma pilha para verificar se uma expressão aritmética é válida.
A expressão é válida se para cada parêntese aberto houver um parêntese fechado correspondente e, 
para cada operação matemática, houver dois operandos.
'''

from Classic_Stack import Pilha

def verificar_expressao_valida(expressao):
    pilha = Pilha()

    for caractere in expressao:
        if caractere == '(':
            pilha.push(caractere)
        elif caractere == ')':
            if pilha.is_empty() or pilha.pop() != '(':
                return False
        elif caractere.isdigit() or caractere in '+-*/':
            continue

    return pilha.is_empty()

expressao = input("Digite uma expressão: ")

if verificar_expressao_valida(expressao):
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")

