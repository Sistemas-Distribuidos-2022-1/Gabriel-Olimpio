import socket

HOST = 'localhost'
PORT = 20000

#objeto socket
#parâmetros:
#família, tipo de protocolo
#IPV4, TCP = STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#recebe um único parâmetro dividido em duas partes
#host, porta
s.bind((HOST, PORT))

#modo de escuta
s.listen()

print('Aguardando conexão de um cliente')

#variáveis conexão e endereço
#método que aceita a conexão
conn, ender = s.accept()

#descobre se a conexão foi aceita e qual é a porta que foi conectada
print('Conectado em', ender)

#agora é a troca de mensagens
while True:
    #data decebe o método receive
    #que recebe o tamanho máximo de bytes que se espera receber
    data = conn.recv(1024)

    #verificar quando terminamos de receber os dados
    if not data:
        print('Fechando a conexão')
        conn.close()
        break

    #
    data = data.decode()

    nome, saldoMedio = data.split(' ')

    saldoMedio = float(saldoMedio)

    if 0 <= saldoMedio <= 200:
        data = 0
    elif 200 <= saldoMedio <= 400:
        data = saldoMedio * 0.2
    elif 401 <= saldoMedio <= 600:
        data = saldoMedio * 0.3
    else:
        data = saldoMedio * 0.4

    #envia de volta para o cliente os dados
    conn.sendall(str.encode(str(data)))
