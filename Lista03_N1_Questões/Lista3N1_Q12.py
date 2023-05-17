'''
Escreva um programa que leia uma string contendo números e 
use uma pilha para converter a string em um número decimal.
'''

from Classic_Stack import Pilha

def str_decimal(string):
    pilha = Pilha()
    decimal = 0

    for caractere in string:
        if caractere.isdigit():
            pilha.push(caractere)

    expoente = 0
    while not pilha.is_empty():
        digito = int(pilha.pop())
        decimal += digito * (10 ** expoente)
        expoente += 1

    return decimal

string = input("Digite uma string contendo números: ")
numero_decimal = str_decimal(string)

print("Número decimal:", numero_decimal)
