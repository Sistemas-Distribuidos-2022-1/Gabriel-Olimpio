import zmq
import time
import random

context = zmq.Context()
s = context.socket(zmq.PUB)  # create a publisher socket
p = "tcp://*:6666"  # how and where to communicate
s.bind(p)  # bind socket to the address

while True:
    time.sleep(5)  # wait every 5 seconds
    nome = "Zezé"
    cargo = random.choice(["operador", "programador"])
    sexo = 'M'
    sal = 1000
    s.send_string(
        "REAJUSTE ,{" + f"'nome': '{nome}', 'salario': {sal}, 'cargo':'{cargo}'" + "}")
