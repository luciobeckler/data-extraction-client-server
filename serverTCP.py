# -- coding: utf-8 --


# -- Gerando os dados a serem consultados
dataBase = [{'ID':0 ,'NAME':'Ana','CPF':14485403678},
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

def findColumnByID(target, idNumber):
      print(dataBase[idNumber][target])


def findID(target,idNumber):
      idNumber = int(idNumber)
      if (int(idNumber)<=len(dataBase)-1): findColumnByID(target,int(idNumber))
      else: print('abc')

while True:
      connectionSocket, clientsocket = serverSocket.accept()
      print("Conectado à: ", clientsocket)

      while True:
            operacao = connectionSocket.recv(1024)
            if not operacao: break
            idNumber = int(connectionSocket.recv(1024))
            

            if str(operacao, 'utf-8')=='NAME': 
                  findID('NAME', idNumber)
            elif str(operacao, 'utf-8')=='CPF': 
                  findID('CPF', idNumber)

            print(clientsocket, " enviou a mensagem: ", str(operacao, 'utf-8'))
            modifiedMessage = operacao.upper() #transforma a mensagem em caixa alta.
            connectionSocket.send(modifiedMessage)
      print("Conexão com o cliente ", clientsocket, " encerrada!")
      connectionSocket.close()


