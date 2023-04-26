# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números pares.

lista = int(input('Digite o tamanho da lista: '))

pares = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num % 2 == 0:
        pares.append(num)

# 'sum' é uma função para somar os elementos de uma lista.
soma = sum(pares)

print('A soma dos numeros pares é igual a: ', soma)
