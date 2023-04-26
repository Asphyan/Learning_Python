'''
Peça para o usuário digitar 5 números e crie uma lista com esses números. 
Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista.
'''

print('Crie uma lista com 5 números\n')

lista = []

# Adicionando os 5 primeiros números
for i in range(5):
    num = int(input(f'Digite o {i+1}° número aqui: '))
    lista.append(num)
print(lista)

# Novo número.
print('\nObrigado por digitar os 5 números!')
print('Agora por favor')
new_num = int(input('\nDigite um novo número: '))
lista.append(new_num)
print(lista)
