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
nivel = input('Digite o nivel (A/B/C/D): ')
salBruto = input('Digite o salBruto: ')
numDependentes = input('Digite o número de dependentes: ')

msg = str(nome + ' ' + nivel + ' ' + salBruto + ' ' + numDependentes)

#envia os dados para o servidor
#encode codifica em formato string
s.sendall(str.encode(msg))

#recebe os dados ecoados até um tamanho de bytes especificado
data = s.recv(1024)

data = data.decode()

print('Nome: ' + nome)
print('Nível: ' + nivel)
print('Salário líquido do funcionário: ', float(salBruto) - float(data))
