from Classic_Queue_Q01 import Fila

fila = Fila()

while True:
    numero = int(input("Digite um número inteiro (ou um número negativo para encerrar): "))
    if numero < 0:
        break
    fila.inserir(numero)

print("Elementos da fila:")
while not fila.vazia():
    elemento = fila.remover()
    print(elemento)
