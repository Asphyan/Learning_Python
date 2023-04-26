# Crie um programa que leia uma lista de números do usuário e exiba o produto desses números.

lista = int(input('Digite o tamanho da lista: '))

produto = 1
numeros = []

for i in range(lista):
    num = float(input(f'Digite o {i+1}° número: '))
    numeros.append(num)

for i in numeros:
    # Ou 'produto *= num'
    produto = produto * num

print(f'O produto da sua lista de números: {numeros} = ', produto)
