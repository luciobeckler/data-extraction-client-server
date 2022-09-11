# -- coding: utf-8 --


# -- Gerando os dados a serem consultados
dados = [{'ID':0 ,'NAME':'Ana','CPF':14485403678},
            {'ID':1,'NAME':'Jose','CPF':18885403678},
            {'ID':2 ,'NAME':'Marcos','CPF':14485479625},
            {'ID':3 ,'NAME':'Lucas ','CPF':14475458698},
            {'ID':4 ,'NAME':'Arnaldo ','CPF':15144758698}]


import socket
HOST = '' 
serverPort = 12000 #definição da porta do servidor. 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o objeto serverSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
serverSocket.bind((HOST,serverPort)) #Faz a ligação no serverSocket a porta designada.

serverSocket.listen(1) #O servidor fica escutando as possíveis conexões e o número indica o número máximo de conexões em fila. Neste caso 1.
print ("Servidor Ativo!")
while True:
      connectionSocket, clientsocket = serverSocket.accept()
      print("Conectado à: ", clientsocket)

      while True:
            operacao = connectionSocket.recv(1024)
            if not operacao: break
            print(operacao)
            idNumber = connectionSocket.recv(1024)
            if not idNumber: break
            print(idNumber)

            print(clientsocket, " enviou a mensagem: ", str(operacao, 'utf-8'))
            modifiedMessage = operacao.upper() #transforma a mensagem em caixa alta.
            connectionSocket.send(modifiedMessage)
      print("Conexão com o cliente ", clientsocket, " encerrada!")
      connectionSocket.close()


