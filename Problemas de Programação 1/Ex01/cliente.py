import socket

HOST = 'localhost'
PORT = 20000

#objeto socket
#parâmetros:
#família, tipo de protocolo
#IPV4, TCP = STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conecta o socket ao servidor ( )
s.connect((HOST, PORT))

#leitura dos dados
nome = input('Digite o nome: ')
cargo = input('Digite o cargo (operador/programador): ')
sal = input('Digite o salário: ')

msg = str(nome + ' ' + cargo + ' ' + sal)

#envia os dados para o servidor
#encode codifica em formato string
s.sendall(str.encode(msg))

#recebe os dados ecoados até um tamanho de bytes especificado
data = s.recv(1024)

data = data.decode()
nome, cargo, sal = data.split(' ')

print('Nome: ', nome)
print('Salário reajustado: ', sal)
