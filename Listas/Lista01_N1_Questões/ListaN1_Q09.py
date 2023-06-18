# Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista.

x = int(input('Digite o tamanho da lista: '))

numeros = []

for i in range (x):
    num = float(input(f'Digite o {i+1}° número: '))
    numeros.append(num)

menor_numero = numeros[0]

# Nesse for 'i' está assumindo o valor do primeiro elemento da lista numeros.
for i in numeros:
    if i < menor_numero:
        menor_numero = i

print ('O menor número da lista é: ', menor_numero)
