'''
Crie um dicionário vazio. 
Peça para o usuário digitar as chaves e os valores desse dicionário.
Em seguida, adicione uma nova chave e valor ao dicionário. 
A chave é 'cidade' e o valor é a cidade em que o usuário nasceu.
'''

dic = {}

quant = int(input('Digite o número de chaves: '))

for i in range(quant):
    chave = input(f'Digite sua chave - {i+1}: ')
    valor = input(f'Valor da chave - {i+1}: ')
    dic[chave] = valor

cid = input(('Digite o nome da cidade em que nasceu: '))
dic['Cidade'] = cid

print(dic)
