'''
Crie um dicionário vazio.
Peça para o usuário digitar as chaves e os valores desse dicionário.
Em seguida, verifique se a chave 'profissão' está presente no dicionário.
'''

dic = {}

print('Criador de dicionário em Python.\n')

quant = int(input('Digite quantas chave/valor quer adicionar: '))

for i in range(quant):
    chave = input('Digite sua chave: ')
    valor = float(input('Digite um número: '))
    dic[chave] = valor

if 'profissão' in dic:
    print("A chave 'profissão' está presente no dicionário.")
else:
    print("A chave 'profissão' não está presente no dicionário.")
