'''
Escreva um programa que use uma pilha para converter um número decimal para hexadecimal.
'''

from Classic_Stack import Pilha

def decimal_hexadecimal(decimal):
    pilha = Pilha()
    hex_letras = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    if decimal == 0:
        pilha.push(0)

    while decimal > 0:
        resto = decimal % 16
        if resto >= 10:
            resto = hex_letras[resto]
        pilha.push(resto)
        decimal = decimal // 16

    hexadecimal = ''
    while not pilha.is_empty():
        hexadecimal += str(pilha.pop())

    return hexadecimal

decimal = int(input("Digite um número decimal: "))
hexadecimal = decimal_hexadecimal(decimal)
print("Hexadecimal:", hexadecimal)

