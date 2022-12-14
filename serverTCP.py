# -- coding: utf-8 --
from operator import mod
import socket

#DECLARANDO FUNÇÕES##################################################################################################################


#FUNÇÕES PARA O FUNCIONAMENTO DO RSA####################################################################################################

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
      criptMessage = phraseToASCII(str(message))
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


#FUNÇÕES EXCLUSIVAS DO SERVIDOR##########################################################################################################
def findColumnByID(target, idNumber):
      return(dataBase[idNumber][target])

def findID(target,idNumber):
      idNumber = int(idNumber)
      if (int(idNumber)<=len(dataBase)-1): return(findColumnByID(target,int(idNumber)))
      else:
            modifiedMessage = 'ID invalido.'
            connectionSocket.send(modifiedMessage.encode())

            operacao = connectionSocket.recv(1024)
            idNumber = connectionSocket.recv(1024)
            findID(operacao,idNumber)

def sendPublicKeys(n,e): #Envia para o cliente as chaves públicas do servidor##################################################################################################################
      n = str(n)
      e = str(e)
      connectionSocket.send(n.encode())
      connectionSocket.send(e.encode())


#CÓDIGO PRINCIPAL##################################################################################################################
# -- Gerando os dados a serem consultados
dataBase = [{'ID':0 ,'NAME':'Ana','CPF':14485403678},
            {'ID':1,'NAME':'Jose','CPF':18885403678},
            {'ID':2 ,'NAME':'Marcos','CPF':14485479625},
            {'ID':3 ,'NAME':'Lucas ','CPF':14475458698},
            {'ID':4 ,'NAME':'Arnaldo ','CPF':15144758698}]
HOST = '' 
serverPort = 12000 #definição da porta do servidor. 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o objeto serverSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
serverSocket.bind((HOST,serverPort)) #Faz a ligação no serverSocket a porta designada.

serverSocket.listen(1) #O servidor fica escutando as possíveis conexões e o número indica o número máximo de conexões em fila. Neste caso 1.
print ("Servidor Ativo!")

nServer,zServer,eServer,dServer = findParameters(17,23)  #Encontra os parâmetros para a criptografia RSA


while True:
      connectionSocket, clientsocket = serverSocket.accept()
      print("Conectado à: ", clientsocket)
      sendPublicKeys(nServer,eServer)
      nClient = int(connectionSocket.recv(1024))
      eClient = int(connectionSocket.recv(1024))

      while True:
            operacao = str(connectionSocket.recv(1024), 'utf-8')
            operacao = descript(dServer,nServer,operacao)
            if not operacao: break
            idNumber = str(connectionSocket.recv(1024), 'utf-8')
            idNumber = descript(dServer,nServer, idNumber)
            
            if operacao=='NAME': 
                  modifiedMessage =  findID('NAME', idNumber)
                  print(clientsocket, " enviou uma requisição de consulta ", operacao, "no ID", idNumber)
                  modifiedMessage = cript(eClient,nClient, modifiedMessage)
                  connectionSocket.send(modifiedMessage.encode())
            elif operacao=='CPF': 
                  modifiedMessage = findID('CPF', idNumber)
                  print(clientsocket, " enviou uma requisição de consulta ", operacao, "no ID", idNumber)
                  modifiedMessage = cript(eClient,nClient, modifiedMessage)
                  connectionSocket.send(str(modifiedMessage).encode())

      print("Conexão com o cliente ", clientsocket, " encerrada!")
      connectionSocket.close()