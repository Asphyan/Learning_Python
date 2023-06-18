'''
Escreva um programa que leia uma expressão matemática na forma de string 
e utilize uma pilha para calcular o resultado da expressão na notação polonesa reversa.
'''

from Classic_Stack import Pilha

def polon_revers(expressao):
    pilha = Pilha()
    operadores = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b,
                  '/': lambda a, b: a / b}

    for caractere in expressao:
        if caractere.isdigit():
            pilha.push(int(caractere))
        elif caractere in operadores:
            operando2 = pilha.pop()
            operando1 = pilha.pop()
            resultado = operadores[caractere](operando1, operando2)
            pilha.push(resultado)

    return pilha.pop()

expressao = input('Digite a expressão em polonesa reversa: ')
result = polon_revers(expressao)

print('Resultado:', result)

'''
'Lambda' é uma função anônima em Python.
É uma forma concisa de definir uma função de forma inline, sem atribuí-la a um nome.
Uma função lambda pode ter qualquer número de argumentos, mas deve ter apenas uma expressão.
A expressão é avaliada e o resultado é retornado automaticamente.
'''
