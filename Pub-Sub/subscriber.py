import zmq

context = zmq.Context()
s = context.socket(zmq.SUB)  # create a subscriber socket
p = "tcp://localhost:6666"  # how and where to communicate
s.connect(p)  # connect to the server
s.subscribe("REAJUSTE")

for i in range(3):  # Three iterations
    recebe = s.recv()  # receive a message
    #resp = eval(recebe)
    if cargo == "operador":
        sal *= 1.2
    if cargo == "programador":
        sal *= 1.18
    printf(f'Nome: {nome}, salario reajustado: {sal}')
