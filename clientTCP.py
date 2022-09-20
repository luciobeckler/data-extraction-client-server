#DECLARANDO FUNÇÕES###############################################################################################################

#FUNÇÕES PARA O FUNCIONAMENTO DO RSA#####################################################################################################
def phraseToASCII(phrase):  #ENTRADA: string qualquer  //  SAIDA: lista de caracteres codificados em ASCII
      asciiCode = list(phrase) #Separa as letras da frase fornecida e armazena numa lista chamada words
      for i in range (len(asciiCode)):
            asciiCode[i] = ord(asciiCode[i]) #Converte os caracteres para seus respectivos códigos ASCII
      return(asciiCode)

def ASCIItophrase(asciiCode): #ENTRADA: lista de caracteres codificados em ASCII //  SAIDA: string qualquer
      phrase = asciiCode
      for i in range (len(phrase)): 
            phrase[i]=chr(phrase[i]) #Converte os códigos ASCII para seus respectivos caracteres
      return ("".join(phrase)) #Junta as letras em uma única frase


def dividers(div): #Encontra e retorna em um array todos os divisores do número fornecido por div#############################################################
      divArray=[]
      i=1
      while (div>=i):
            if(div%i==0):
                  divArray.append(i)
            i+=1
      return(divArray)

def findMDC(arrayA, arrayB): #Encontra o maior valor em comum entre dois arrays fornecidos###############################################################
      maxDivisor = 0
      for i in range (len(arrayA)): 
            for j in range(len(arrayB)):
                  if(arrayA[i]==arrayB[j]): maxDivisor = arrayA[i]
      return(maxDivisor)

def mdc(a,b):  #Encontra o máximo divisor comum entre dois números (a e b)#########################################################################
      aDividers = dividers(a)
      bDividers = dividers(b)
      return(findMDC(aDividers,bDividers))

def findE(n):  #Encontra o valor e, ou seja, o menor coprimo do valor fornecido ao chamar a função#########################################################################
     while True:
            e=2
            if(mdc(n,e)==1): return 3
            e+=1

def findD(e,z): #Encontra o valor de d em função de e e z###############################################################################################
      d=0
      while((e*d)%z!=1):
            d+=1
      return d

def cript(e, n, message): #Recebe duas chaves públicas e uma string e retorna outra string contendo a mensagem criptografada#######################################
      criptMessage = phraseToASCII(message)
      for i in range (len(criptMessage)):
            criptMessage[i] = (criptMessage[i]**e)%n
      return (" ".join(map(str,criptMessage))) #Retorna a mensagem criptografada em forma de uma variável do tipo STR

def descript(d,n,message): ##Recebe duas chaves privadas e uma string encriptada e retorna outra string contendo a mensagem descriptografada#######################################
      descriptMessage = message.split()
      for i in range (len(descriptMessage)):
            descriptMessage[i] = int(descriptMessage[i])
            descriptMessage[i] = descriptMessage[i]**d%n
      descriptMessage = ASCIItophrase(descriptMessage)
      return descriptMessage

        

def findParameters(p,q):
      n = p*q
      z = (p-1)*(q-1) 
      e = findE(n)
      d = findD(e,z)
      return(n,z,e,d)

def sendPublicKeys(n,e): #Envia para o Client as chaves públicas do servidor##################################################################################################################
      n = str(n)
      e = str(e)
      clientSocket.send(n.encode())
      clientSocket.send(e.encode())

#FUNÇÕES EXCLUSIVAS DO Client##########################################################################################################
def sendToServer(column, idNumber):  #Envia os valores passados como parâmetro para o servidor, recebe e exibe a resposta do mesmo
      sendPublicKeys(nClient,eClient)
      sendMessage = cript(eServer, nServer, column)
      clientSocket.send(str.encode(sendMessage)) #clientSocket.send(msg) #Cria o segmento TCP com os dados (variável message) e o cabeçalho com o número do servidor e da porta. A porta do Client no TCP não é explícita, é determinada pelo S.O. 
      sendMessage = cript(eServer,nServer,idNumber)
      clientSocket.send(str.encode(sendMessage))
      modifiedMessage = clientSocket.recv(1024) #Aguarda e recebe uma resposta do servidor
      modifiedMessage = descript(dClient, nClient, modifiedMessage)

      print ("\nO nome/CPF do usuário de ID "+idNumber+' é:')
      print(modifiedMessage)


def userRequest(): #Função responsável por adquirir os parâmetros que o usuário deseja consultar, garantir que eles estejam corretos e encerrar o programa 
      finishProgram = input('\nDeseja encerrar o programa:')
      
      
      while ((finishProgram!='Sim') and (finishProgram!='Nao')): finishProgram = input('Responda com Sim ou Nao:')

      while finishProgram=='Nao':
            column = input('Qual coluna deseja consultar:')
            while ((column!='NAME') and (column!='CPF')): column = input('Selecione uma coluna válida(NAME / CPF):')

            idNumber = input('Para qual ID deseja realizar a consulta? \n Insira um valor inteiro entre 0 e 4:')

            print(column, idNumber)
            sendToServer(column, idNumber)
            finishProgram = input('\nDeseja encerrar o programa:')
            while ((finishProgram!='Sim') and (finishProgram!='Nao')): finishProgram = input('Responda com Sim ou Nao:')
      return()


# -- coding: utf-8 --
import socket
HOST = '127.0.0.1' #Pode ser tanto um endereço IP ou um nome(neste caso será necessário uma consulta DNS.)
serverPort = 12000 #define a porta de acesso no servidor TCP.
clientSocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET (para IPv4) - SOCK_STREAM (Indica conexão TCP)

clientSocket.connect((HOST, serverPort)) #cria o objeto clientSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
print('Conectado ao servidor:', serverPort)
nServer = int(clientSocket.recv(1024))
eServer = int(clientSocket.recv(1024))

nClient,zClient,eClient,dClient = findParameters(29,11)  #Encontra os parâmetros para a criptografia RSA
userRequest()
print('conexao encerrada')
clientSocket.close()