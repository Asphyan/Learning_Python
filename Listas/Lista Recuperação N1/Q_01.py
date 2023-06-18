'''
Uma empresa deseja verificar se um determinado cupom está dentro da faixa de cupons gerados para a promoção de São João.
Caso o número esteja dentro do intervalo, o programa deve exibir a mensagem "Cupom válido".
Caso contrário, deve exibir a mensagem "Cupom inválido", sabendo que o primeiro cupom tinha o número 75 e o último gerado foi o 208.
Escreva um programa em Python que recebe o número inteiro do cupom e verifique se o cupom é válido.
'''

print('## Promoção de São João ##')
print('\nVerifique se seu cumpom é valido em nossa promoção!')

cup = int(input('\nDigite o número do seu cupom aqui: '))

if  75 <= cup <= 208:
    print('Cupom válido!')
else:
    print('Cupom inválido')
    