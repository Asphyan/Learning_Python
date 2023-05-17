'''
Escreva um programa que use uma pilha para converter um número binário para octal.
'''

from Classic_Stack import Pilha

def bin_octal(binario):
    pilha = Pilha()
    octal = ''

    if len(binario) % 3 != 0:
        binario = '0' * (3 - (len(binario) % 3)) + binario

    for i in range(0, len(binario), 3):
        grupo = binario[i:i+3]
        pilha.push(grupo)

    while not pilha.is_empty():
        grupo = pilha.pop()
        digito_octal = int(grupo, 2)
        octal = str(digito_octal) + octal

    return octal

binario = input("Digite um número binário: ")
num_octal = bin_octal(binario)

print("Número octal:", num_octal)
