'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.
'''

lista = []

print('Digite 3 nomes.\n')

for i in range(3):
    nome = input(f'Digite o {i+1}° nome: ')
    lista.append(nome)

tt = tuple(lista)

quant = tt.count('Maria')

print(quant)
