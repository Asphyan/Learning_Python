'''
Escreva um programa que use uma pilha para converter um número decimal para binário.
'''

from Classic_Stack import Pilha

def decimal_para_binario(numero):
    pilha = Pilha()

    if numero == 0:
        pilha.push(0)

    while numero > 0:
        bit = numero % 2
        pilha.push(bit)
        numero //= 2

    binario = ''
    while not pilha.is_empty():
        binario += str(pilha.pop())

    return binario

numero_decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(numero_decimal)
print("Número binário:", binario)
