'''
Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes.
Em seguida, peça para o usuário escolher um dos nomes e substituir esse nome por outro nome que ele também deve digitar.
'''

print('Por favor digite 3 nomes.')

lista = []

# Digite os 3 nomes.
for i in range(3):
    nome = input(f'Digite o {i+1}° nome: ')
    lista.append(nome)

tt = tuple(lista)
print(tt)

# Editar.
print('\nAgora edite um dos nomes!\n')
index = int(input('Digite o indice do nome a ser editado: '))

if index < len(lista):
    nome = input('\nDigite o novo nome: ')
    lista[index] = (nome)
    tt = tuple(lista)

print(tt)