# Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a".

lista = int(input('Digite o tamanho da lista: '))

palavras = []

for i in range(0, lista):
    palavra = input(f'Digite a {i+1}° palavra: ')
    if palavra[0] == 'a':
        palavras.append(palavra)

print(palavras)
