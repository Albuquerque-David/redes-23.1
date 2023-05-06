from socket import *

PORT = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', PORT))

tradutor  = {'PORT': 'Porta', 'PROTOCOL':  'Protocolo', 'CLIENT': 'Cliente', 'SERVER': 'Servidor', 'TCP': 'Protocolo de Controle de Transmissão', 
             'UDP': 'Protocolo de Datagrama de Usuário', 'DNS': 'Sistema de Nome de Domínio', 'HTTP': 'Protocolo de Transferência de HiperTexto', 'P2P': 'Par a Par', 'RFC': 'Requisição para Comentários'}

print("Aguardando conexão...")

while True:
    mensagem, enderecoCliente = serverSocket.recvfrom(2048)
    if mensagem.decode().upper() == 'FIM':
        break

    resposta = tradutor.get(mensagem.decode().upper(), "Não foi possível traduzir o termo.")

    serverSocket.sendto(resposta.encode(), enderecoCliente)

serverSocket.close()
    