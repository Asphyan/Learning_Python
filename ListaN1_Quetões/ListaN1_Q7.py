# Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa.

x = int(input("Digite o tamanho da lista de palavras: "))

palavra_mais_longa = ""

#"len" é uma função built-in do Python que retorna o comprimento (número de itens) de um objeto.

for i in range(0, x):
    palavra = input(f'Digite a {i+1}° palavra: ')
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra

print("A palavra mais longa é:", palavra_mais_longa)
