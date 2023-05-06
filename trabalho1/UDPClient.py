from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Entre com uma mensagem: ')
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    if message.upper() == 'FIM':
        break

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

clientSocket.close()