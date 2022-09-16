def phraseToASCII(phrase):  #ENTRADA: string qualquer  //  SAIDA: lista de caracteres codificados em ASCII
      asciiCode = list(phrase) #Separa as letras da frase fornecida e armazena numa lista chamada words
      for i in range (len(asciiCode)):
            asciiCode[i] = ord(asciiCode[i]) #Converte os caracteres para seus respectivos códigos ASCII
      return(asciiCode)

def ASCIItophrase(asciiCode):
      phrase = asciiCode
      for i in range (len(phrase)): #ENTRADA: lista de caracteres codificados em ASCII //  SAIDA: string qualquer
            phrase[i]=chr(phrase[i]) #Converte os códigos ASCII para seus respectivos caracteres
      return (" ".join(phrase)) #Junta as letras em uma única frase