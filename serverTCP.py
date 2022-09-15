# -- coding: utf-8 --


# -- Gerando os dados a serem consultados
dataBase = [{'ID':0 ,'NAME':'Ana','CPF':14485403678},
            {'ID':1,'NAME':'Jose','CPF':18885403678},
            {'ID':2 ,'NAME':'Marcos','CPF':14485479625},
            {'ID':3 ,'NAME':'Lucas ','CPF':14475458698},
            {'ID':4 ,'NAME':'Arnaldo ','CPF':15144758698}]


from operator import mod
import socket
HOST = '' 
serverPort = 12000 #definição da porta do servidor. 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o objeto serverSocket. AF_INET => Constante que indica IPv4. | SOCK_STREAM => Constante que indica que é um Segmento TCP.
serverSocket.bind((HOST,serverPort)) #Faz a ligação no serverSocket a porta designada.

serverSocket.listen(1) #O servidor fica escutando as possíveis conexões e o número indica o número máximo de conexões em fila. Neste caso 1.
print ("Servidor Ativo!")

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

def cript(e, n, message):
      criptMessage = (message**e)%n
      return criptMessage

def descript(d,n,message):
      descriptMessage = message**d%n
      return descriptMessage
        
def findParameters(p,q):
      n=p*q

p=17
q=23
n=p*q #35
print('n=',n)
z = (p-1)*(q-1) #24
print('z=',z)
e = findE(n) #2
print('e=',e)
d = findD(e,z) #12
print('d=',d)
print('109 criptografado da:',cript(e,n,109))
print('37 descriptografado da:', descript(d,n,37))


while True:
      connectionSocket, clientsocket = serverSocket.accept()
      print("Conectado à: ", clientsocket)

      while True:
            operacao = connectionSocket.recv(1024)
            if not operacao: break
            idNumber = connectionSocket.recv(1024)
            print(idNumber)
            

            if str(operacao, 'utf-8')=='NAME': 
                  modifiedMessage =  findID('NAME', idNumber)
                  print(clientsocket, " enviou uma requisição de consulta ", str(operacao, 'utf-8'), "no ID", str(idNumber, 'utf-8'))
                  connectionSocket.send(modifiedMessage.encode())
            elif str(operacao, 'utf-8')=='CPF': 
                  modifiedMessage = str(findID('CPF', idNumber))
                  print(clientsocket, " enviou uma requisição de consulta ", str(operacao, 'utf-8'), "no ID", str(idNumber, 'utf-8'))
                  connectionSocket.send(modifiedMessage.encode())

      print("Conexão com o cliente ", clientsocket, " encerrada!")
      connectionSocket.close()





