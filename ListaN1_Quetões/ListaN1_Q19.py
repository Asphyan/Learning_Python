# Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente.

lista = int(input('Digite o tamanho da lista: '))

numeros = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    numeros.append(num)

# Função sort é usada para ordenar a lista. Para ondená-los em outra variável usar 'crescente = sorted(numeros)'
numeros.sort()

print('Lista de números em ordem crescente: ', numeros)
