'''
Escreva um programa que leia uma string contendo números 
e use uma pilha para converter a string em um número binário.
'''

from Classic_Stack import Pilha

def str_binario(string):
    pilha = Pilha()
    binario = ''

    for caractere in string:
        if caractere.isdigit():
            pilha.push(caractere)

    while not pilha.is_empty():
        digito = int(pilha.pop())
        binario += str(digito % 2)

    return binario

string = input("Digite uma string contendo números: ")
num_bin = str_binario(string)

print("Número binário:", num_bin)
