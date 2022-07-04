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
altura = input('Digite a altura: ')
peso = input('Digite o peso: ')
sexo = input('Digite o sexo (M/F): ')

msg = str(altura + ' ' + peso + ' ' + sexo)

#envia os dados para o servidor
#encode codifica em formato string
s.sendall(str.encode(msg))

#recebe os dados ecoados até um tamanho de bytes especificado
data = s.recv(1024)

data = data.decode()

print('Peso ideal: ', data)
