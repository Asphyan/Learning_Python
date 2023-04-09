# Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista.

maior_numero = 0

x = int(input('Digite o tamanho da lista: '))

for i in range(0, x):
    z = int(input(f'Digite o {i+1}° número: '))
    if z > maior_numero:
        maior_numero = z

print(maior_numero)
