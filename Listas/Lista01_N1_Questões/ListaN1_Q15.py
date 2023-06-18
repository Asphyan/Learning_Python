# Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5.

lista = int(input('Digite o tamanho da lista: '))

numero_menor_que_5 = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num < 5:
        numero_menor_que_5.append(num)

print(numero_menor_que_5)
