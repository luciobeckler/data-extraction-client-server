

from cmath import exp


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






# chr(n) retorna o caracter correspondente ao código n
# ord(n) retorna o numero correspondente ao caractere n

