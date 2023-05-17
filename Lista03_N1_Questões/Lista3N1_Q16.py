'''
Escreva um programa que use uma pilha para converter um número hexadecimal para decimal.
'''

from Classic_Stack import Pilha

def hex_dec(hexadecimal):
    pilha = Pilha()
    decimal = 0

    for caractere in hexadecimal:
        if caractere.isdigit():
            pilha.push(int(caractere))
        elif caractere.isalpha():
            valor = ord(caractere.upper()) - ord('A') + 10
            pilha.push(valor)

    expoente = 0
    while not pilha.is_empty():
        digito = pilha.pop()
        decimal += digito * (16 ** expoente)
        expoente += 1

    return decimal

hex = input("Digite um número hexadecimal: ")
num_dec = hex_dec(hex)

print("Número decimal:", num_dec)
