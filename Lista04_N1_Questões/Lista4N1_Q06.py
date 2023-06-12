from Classic_Queue_Q01 import Fila
import time

fila_atendimento = Fila()

def chegada_cliente(cliente_id):
    fila_atendimento.inserir(cliente_id)

def atender_proximo_cliente():
    if not fila_atendimento.vazia():
        proximo_cliente = fila_atendimento.remover()
        print("Atendendo cliente:", proximo_cliente)
    else:
        print("Não há clientes na fila de atendimento.")

chegada_cliente(1)
chegada_cliente(2)
chegada_cliente(3)
chegada_cliente(4)
chegada_cliente(5)

# Simulação de atendimento a cada hora
for hora in range(1, 6):
    print("Hora:", hora)
    atender_proximo_cliente()
    print("---")
    time.sleep(1)  # Simula a passagem de hora usando time.sleep()

