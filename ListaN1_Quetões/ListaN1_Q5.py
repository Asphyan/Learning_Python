# Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar.

x = int(input('Digite um número: '))

if x % 2 == 0:
    print(x, '-', 'É é par.')
else:
    print(x, '-', 'É é impar.')
