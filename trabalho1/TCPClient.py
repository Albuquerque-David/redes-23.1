from socket import *

HOST = '127.0.0.1'
PORT = 11000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((HOST, PORT))

while True:
    message = input('Entre com uma palavra: ')

    clientSocket.send(message.encode())

    if message.upper() == 'FIM':
        break

    resposta = clientSocket.recv(1024)

    print(str(resposta, encoding='utf-8'))

clientSocket.close()
