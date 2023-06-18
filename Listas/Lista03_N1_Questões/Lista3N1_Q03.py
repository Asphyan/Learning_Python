'''
Escreva um programa que leia uma string contendo números e operações matemáticas (+, -, *, /)
e use uma pilha para calcular o resultado da expressão.
'''

from Classic_Stack import Pilha

def calcular(expressao):
    operadores = Pilha()
    numeros = []
    resultado = 0
    numero_atual = ''

    for caracter in expressao:
        if caracter.isdigit():
            numero_atual += caracter
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            if numero_atual:
                numeros.append(float(numero_atual))
                numero_atual = ''
            while not operadores.is_empty() and operadores.top() != '(':
                calcular_operacao(operadores, numeros)
            operadores.pop()
        elif caracter in '+-*/':
            if numero_atual:
                numeros.append(float(numero_atual))
                numero_atual = ''
            while not operadores.is_empty() and obter_precedencia(caracter) <= obter_precedencia(operadores.top()):
                calcular_operacao(operadores, numeros)
            operadores.push(caracter)

    if numero_atual:
        numeros.append(float(numero_atual))

    while not operadores.is_empty():
        calcular_operacao(operadores, numeros)

    if len(numeros) == 1:
        resultado = numeros[0]

    return resultado


def calcular_operacao(operadores, numeros):
    operador = operadores.pop()
    num2 = numeros.pop()
    num1 = numeros.pop()

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2

    numeros.append(resultado)

def obter_precedencia(operador):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedencia.get(operador, 0)

expressao = input("Digite uma expressão matemática: ")
resultado = calcular(expressao)
print("Resultado:", resultado)
