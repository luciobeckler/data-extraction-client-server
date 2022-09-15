# -- coding: utf-8 --
import socket
HOST = '127.0.0.1' #Pode ser tanto um endereço IP ou um nome(neste caso será necessário uma consulta DNS.)
serverPort = 12000 #define a porta de acesso no servidor TCP.
clientSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (para IPv4) - SOCK_STREAM (Indica conexão TCP)

clientSocket.connect((HOST, serverPort)) #cria o objeto clientSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
print('Conectado ao servidor:', serverPort)


#DECLARANDO FUNÇÕES###############################################################################################################
def sendToServer(column, idNumber):  #Envia os valores passados como parâmetro para o servidor, recebe e exibe a resposta do mesmo
      clientSocket.send(str.encode(column))
      #clientSocket.send(msg) #Cria o segmento TCP com os dados (variável message) e o cabeçalho com o número do servidor e da porta. A porta do cliente no TCP não é explícita, é determinada pelo S.O. 
      clientSocket.send(str.encode(idNumber))
      modifiedMessage = clientSocket.recv(1024) #Aguarda e recebe uma resposta do servidor

    
      #clientSocket.send(msg) #Cria o segmento TCP com os dados (variável message) e o cabeçalho com o número do servidor e da porta. A porta do cliente no TCP não é explícita, é determinada pelo S.O. 



      print ("\nO nome/CPF do usuário de ID "+idNumber+' é:')
      print(modifiedMessage)


def userRequest(): #Função responsável por adquirir os parâmetros que o usuário deseja consultar, garantir que eles estejam corretos e encerrar o programa 
      finishProgram = input('\nDeseja encerrar o programa:')
      
      
      while ((finishProgram!='Sim') and (finishProgram!='Nao')): finishProgram = input('Responda com Sim ou Nao:')

      while finishProgram=='Nao':
            column = input('Qual coluna deseja consultar:')
            while ((column!='NAME') and (column!='CPF')): column = input('Selecione uma coluna válida(NAME / CPF):')

            idNumber = input('Para qual ID deseja realizar a consulta? \n Insira um valor inteiro maior ou igual a 0:')

            print(column, idNumber)
            sendToServer(column, idNumber)
            finishProgram = input('\nDeseja encerrar o programa:')
            while ((finishProgram!='Sim') and (finishProgram!='Nao')): finishProgram = input('Responda com Sim ou Nao:')
      return()



userRequest()
print('conexao encerrada')
clientSocket.close()


