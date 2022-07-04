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

    nome, nivel, salBruto, numDependentes = data.split(' ')

    salBruto = float(salBruto)
    numDependentes = int(numDependentes)

    if nivel == 'A':
        if numDependentes <= 0:
            salBruto *= 0.03
        else:
            salBruto *= 0.08
    elif nivel == 'B':
        if numDependentes <= 0:
            salBruto *= 0.05
        else:
            salBruto *= 0.1
    elif nivel == 'C':
        if numDependentes <= 0:
            salBruto *= 0.08
        else:
            salBruto *= 0.15
    else:
        if numDependentes <= 0:
            salBruto *= 0.1
        else:
            salBruto *= 0.17

    data = str.encode(str(salBruto))

    #envia de volta para o cliente os dados
    conn.sendall(data)
