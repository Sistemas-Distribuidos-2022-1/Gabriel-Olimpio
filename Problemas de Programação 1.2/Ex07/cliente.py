import socket
import json

HOST = 'LocalHost'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print("Digite a Idade do Funcionario: ")
idade = input()

print("Digite o Tempo de Serviço do Funcionario: ")
tempo = input()

json_objeto = {
    "idade": idade,
    "tempo": tempo
}

mensagem = json.dumps(json_objeto)

s.sendall((mensagem+"\n").encode())

json_objeto = s.recv(1024)
resposta = json.loads(json_objeto.decode())

print(resposta["aposentado"])
