'''
Um professor deseja calcular a média de notas de uma turma de 10 alunos.
Escreva um programa em Python que solicite ao professor as notas dos alunos e, em seguida,
calcule e exiba a média das notas.
Utilize um laço de repetição (FOR) para solicitar as notas dos alunos e 
uma variável para armazenar a soma das notas.
'''

j = 0

for i in range(10):
    nota = float(input(f'Digite a {i+1}° nota: '))
    j = nota + j

print('Média Geral dos 10 alunos', j/10)
