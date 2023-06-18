'''
Escreva um programa que use uma pilha para verificar se uma string é um palíndromo 
(ou seja, se é igual quando lida de trás para frente).
'''

from Classic_Stack import Pilha

def verificar_palindromo(num):
    pilha = Pilha()
    num = num.lower().replace(" ", "")

    for caracter in num:
        pilha.push(caracter)

    num_invertido = ''
    while not pilha.is_empty():
        num_invertido += pilha.pop()

    return num == num_invertido

num = input("Digite um número: ")

if verificar_palindromo(num):
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")
