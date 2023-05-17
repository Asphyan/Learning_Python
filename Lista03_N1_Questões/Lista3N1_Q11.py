'''
Escreva um programa que use uma pilha para ordenar uma lista de inteiros em ordem crescente.
'''

from Classic_Stack import Pilha

def ordenar_lista(lista):
    pilha = Pilha()
    lista_ordenada = []

    for i in lista:
        while not pilha.is_empty() and i > pilha.top():
            lista_ordenada.append(pilha.pop())
        pilha.push(i)

    while not pilha.is_empty():
        lista_ordenada.append(pilha.pop())

    return lista_ordenada

quantidade = int(input("Digite o tamanho da lista: "))
lista = []

for i in range(quantidade):
    numero = int(input(f"Digite o número {i+1}: "))
    lista.append(numero)

lista_cres = ordenar_lista(lista)

print("Lista ordem crescente:", lista_cres)
