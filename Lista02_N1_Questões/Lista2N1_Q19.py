'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números.
Em seguida, verifique quantos elementos estão no conjunto.
'''

conj = set([])

print('Digite 5 números\n')

for i in range(5):
    num = float(input(f'Digite o {i+1}° número: '))
    conj.add(num)

print('A quantidade de elementos do conjunto é -', len(conj))
