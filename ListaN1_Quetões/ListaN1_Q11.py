# Crie um programa que leia uma lista de números do usuário e exiba somente os números pares.

lista = int(input('Digite a quantidade de itens da lista: '))

pares = []

for i in range(0, lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num % 2 == 0:
        # (.append) é uma função que adiciona um item à lista existente. Nesse caso pares é a lista/vetor e 'num' é o número adicionado a lista,após passar pela condição do 'if'.
        pares.append(num)

print(pares)
