'''
Escreva um programa que use uma pilha para verificar se uma string é um palíndromo 
(ou seja, se é igual quando lida de trás para frente).
'''

from Classic_Stack import Pilha

def verificar_palindromo(texto):
    pilha = Pilha()
    texto = texto.lower().replace(" ", "")

    for caracter in texto:
        pilha.push(caracter)

    texto_invertido = ''
    while not pilha.is_empty():
        texto_invertido += pilha.pop()

    return texto == texto_invertido

string = input("Digite uma string: ")

if verificar_palindromo(string):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
