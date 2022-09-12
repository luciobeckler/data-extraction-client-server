# -- coding: utf-8 --
import socket
HOST = '127.0.0.1' #Pode ser tanto um endereço IP ou um nome(neste caso será necessário uma consulta DNS.)
serverPort = 12000 #define a porta de acesso no servidor TCP.
clientSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (para IPv4) - SOCK_STREAM (Indica conexão TCP)

clientSocket.connect((HOST, serverPort)) #cria o objeto clientSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
print('Conectado ao servidor:', serverPort, ",\nPara encerrar digite: encerrar")
operacao = input('Informe o dado a ser consultado: ')
idNumber = input('Informe o número do ID a ser consultado: ')

while ((operacao!= 'encerrar') and (idNumber!='encerrar')):
      clientSocket.send(str.encode(operacao))
      #clientSocket.send(msg) #Cria o segmento TCP com os dados (variável message) e o cabeçalho com o número do servidor e da porta. A porta do cliente no TCP não é explícita, é determinada pelo S.O. 
      clientSocket.send(str.encode(idNumber))
    
    
      modifiedMessage = clientSocket.recv(1024) #Aguarda e recebe uma resposta do servidor

    
      #clientSocket.send(msg) #Cria o segmento TCP com os dados (variável message) e o cabeçalho com o número do servidor e da porta. A porta do cliente no TCP não é explícita, é determinada pelo S.O. 



      print ("\nO nome/CPF do usuário de ID "+idNumber+' é:')
      print(modifiedMessage)
 
      operacao = input('Informe o dado a ser consultado: ')
      idNumber = input('Informe o número do ID a ser consultado: ')
print('conexao encerrada')
clientSocket.close()