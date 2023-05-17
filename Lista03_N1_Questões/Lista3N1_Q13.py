'''
Escreva um programa que use uma pilha para converter um número binário para decimal.
'''

from Classic_Stack import Pilha

def bin_dec(numero_binario):
    pilha = Pilha()

    for digito in numero_binario:
        pilha.push(int(digito))

    dec = 0
    expoente = 0

    while not pilha.is_empty():
        bit = pilha.pop()
        dec += bit * (2 ** expoente)
        expoente += 1

    return dec

numero_binario = input("Digite um número binário: ")
decimal = bin_dec(numero_binario)

print("O número decimal correspondente é:", decimal)
