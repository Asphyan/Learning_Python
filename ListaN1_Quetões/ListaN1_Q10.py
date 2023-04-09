# Crie um programa que leia uma lista de números do usuário e exiba a média desses números.

x = int(input('Digite o tamanho da sua lista de números: '))

for i in range(0, x):
    y = float(input(f'Digite o {i+1}° número: '))
    y = y + y

print(y/x)
