"""
Escreva um programa que use uma pilha para converter um número octal para decimal.
"""

from Classic_Stack import Pilha


def oct_dec(octal):
    pilha = Pilha()
    decimal = 0

    for caractere in octal:
        if caractere.isdigit():
            pilha.push(int(caractere))

    expoente = 0
    while not pilha.is_empty():
        digito = pilha.pop()
        decimal += digito * (8**expoente)
        expoente += 1

    return decimal

octal = input("Digite um número octal: ")
num_dec = oct_dec(octal)

print("Número decimal:", num_dec)
