# Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares.

lista = int(input('Digite o tamanho da lista: '))

impares = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    if num % 2 != 0:
        impares.append(num)

soma = sum(impares)

print ('A soma dos números ímpares da sua lista é igual a: ', soma)
