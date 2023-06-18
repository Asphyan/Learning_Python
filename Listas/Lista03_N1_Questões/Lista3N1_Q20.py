'''
Escreva um programa que use uma pilha para converter um número binário para hexadecimal.
'''

from Classic_Stack import Pilha

def bin_hexa(binario):
    pilha = Pilha()
    hexadecimal = ''

    if len(binario) % 4 != 0:
        binario = '0' * (4 - (len(binario) % 4)) + binario

    for i in range(0, len(binario), 4):
        grupo = binario[i:i+4]
        pilha.push(grupo)

    while not pilha.is_empty():
        grupo = pilha.pop()
        digito_hexadecimal = hex(int(grupo, 2))[2:].upper()
        hexadecimal = digito_hexadecimal + hexadecimal

    return hexadecimal

binario = input("Digite um número binário: ")
num_hexa = bin_hexa(binario)

print("Número hexadecimal:", num_hexa)
