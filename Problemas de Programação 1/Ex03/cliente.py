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
N1 = input('Digite a Nota 1: ')
N2 = input('Digite a Nota 2: ')
N3 = input('Digite a Nota 3: ')

msg = str(nome + ' ' + N1 + ' ' + N2 + ' ' + N3)

#envia os dados para o servidor
#encode codifica em formato string
s.sendall(str.encode(msg))

#recebe os dados ecoados até um tamanho de bytes especificado
data = s.recv(1024)

data = data.decode()

if data == 'aprovado':
	print(nome + ' foi aprovado')
else:
	print(nome + ' foi reprovado')
