def phraseToASCII(phrase):  #ENTRADA: string qualquer  //  SAIDA: lista de caracteres codificados em ASCII
      asciiCode = list(phrase) #Separa as letras da frase fornecida e armazena numa lista chamada words
      for i in range (len(asciiCode)):
            asciiCode[i] = ord(asciiCode[i]) #Converte os caracteres para seus respectivos códigos ASCII
      return(asciiCode)

def ASCIItophrase(asciiCode): #ENTRADA: lista de caracteres codificados em ASCII //  SAIDA: string qualquer
      phrase = asciiCode
      for i in range (len(phrase)): 
            phrase[i]=chr(phrase[i]) #Converte os códigos ASCII para seus respectivos caracteres
      return (" ".join(phrase)) #Junta as letras em uma única frase


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
      descriptMessage = message
      for i in range (len(descriptMessage)):
            descriptMessage[i] = descriptMessage[i]**d%n
      descriptMessage = ASCIItophrase(descriptMessage)
      return descriptMessage

        

def findParameters(p,q):
      n = p*q
      z = (p-1)*(q-1) 
      e = findE(n)
      d = findD(e,z)
      return(n,z,e,d)

n,z,e,d = findParameters(17,23)
print(n,z,e,d)
print('frase criptografado da:',cript(e,n,'NAME'))
print('ascii descriptografado da:', descript(d,n,[269, 143, 236, 69]))
print('NAME')

print(type(cript(e,n,'NAME')))






# chr(n) retorna o caracter correspondente ao código n
# ord(n) retorna o numero correspondente ao caractere n

