'''
Uma livraria deseja listar os livros mais vendidos do mês no padrão POSIÇÃO - TÍTULO DO LIVRO. 
Escreva um programa em Python que receba uma lista de livros com sua respectiva posição no ranking dos mais vendidos 
e exiba essa lista em tela, conforme o exemplo a seguir.

Ranking de Mais Vendidos
1 - Senhor dos Anéis
2 - O apanhador no campo de centeio
'''

dic = {}
dic_ordenado = {}



tam = int(input('Digite o tamanho da sua lista: '))

for i in range(tam):
    liv = input('Digite o nome do livro: ')
    rank = int(input('Digite sua posição no ranking: '))
    dic[liv] = rank

for i in sorted(dic, key = dic.get): # key para indicar a chave e get para pegar a chave do dic.
    dic_ordenado[i] = dic[i]

print('Ranking de Mais Vendidos')

for liv, rank in dic_ordenado.items(): # O método "items()" é usado para percorrer as chaves e os valores do dicionário.
    print(f'{rank} - {liv}') # Metodo fstring.

# (Duvidas assistir tutorial novamente) -> https://www.youtube.com/watch?v=1lhYLXpCimI
