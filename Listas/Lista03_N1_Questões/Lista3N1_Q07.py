'''
Escreva um programa que use uma pilha para converter um número decimal para octal.
'''

from Classic_Stack import Pilha

def decimal_octal(decimal):
    pilha = Pilha()

    if decimal == 0:
        pilha.push(0)

    while decimal > 0:
        resto = decimal % 8
        pilha.push(resto)
        decimal = decimal // 8

    octal = ''
    while not pilha.is_empty():
        octal += str(pilha.pop())

    return octal

decimal = int(input("Digite um número decimal: "))
octal = decimal_octal(decimal)
print("Octal:", octal)
