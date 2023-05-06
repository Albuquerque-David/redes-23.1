from socket import *

PORT = 11000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', PORT))

tradutor = {'PORT': 'Porta', 'PROTOCOL':  'Protocolo', 'CLIENT': 'Cliente', 'SERVER': 'Servidor', 'TCP': 'Protocolo de Controle de Transmissão',
            'UDP': 'Protocolo de Datagrama de Usuário', 'DNS': 'Sistema de Nome de Domínio', 'HTTP': 'Protocolo de Transferência de HiperTexto', 'P2P': 'Par a Par', 'RFC': 'Requisição para Comentários'}

print("Aguardando conexão...")

serverSocket.listen(1)
newSocket, enderecoCliente = serverSocket.accept()

while True:
    mensagem = str(newSocket.recv(2048), encoding='utf-8')
    
    if mensagem.upper() == 'FIM':
        break

    resposta = tradutor.get(mensagem.upper(), "Não foi possível traduzir o termo.")
    newSocket.send(resposta.encode())

newSocket.close()
serverSocket.close()
