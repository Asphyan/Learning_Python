'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto.
'''

conj = set([])

for i in range(5):
    num = float(input(f'Digite o {i+1}° número: '))
    conj.add(num)

print(conj)
print('\nEscolha um número para remover.')
rmv = float(input('Digite aqui: '))
conj.remove(rmv)
print(conj)
