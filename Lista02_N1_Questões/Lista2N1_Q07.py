'''
Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
Em seguida, retorne o primeiro elemento da tupla.
'''

print('Por favor digite 5 números.')

lista = []

# Digite os 5 números.
for i in range(5):
    num = input(f'Digite o {i+1}° número: ')
    lista.append(num)

tt = tuple(lista)
first = tt[0]

print('\nO primeiro elemento da tupla é',first)