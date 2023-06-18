# Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10.

lista = int(input('Digite o tamanho da lista: '))

numero_maior_que_10 = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num > 10:
        numero_maior_que_10.append(num)

print(numero_maior_que_10)
