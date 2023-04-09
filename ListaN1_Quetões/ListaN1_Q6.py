# Crie um programa que leia uma lista de números do usuário e exiba a soma desses números.

x = int(input('Digite o tamanho da sua lista de números: '))

for i in range(0, x):
    y = int(input(f'Digite a {i+1}° palavra: '))
    y = y + y

print(y)
