letterGoodness= [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0402, .0241, .0675, .0751, .0193, .0009, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
print(letterGoodness) #testing... it's predefined
inputo= str(input("Insert your encoded word: "))
def ChrReplace(character, loopNo): #get the character and the probabilities of it being another character
   if ord(character) < 65 or ord(character) > 90:
       return character
   ChrNum= ord(character) #Get the chr num
   newChrno= ChrNum + loopNo
   if newChrno > 90:
       newChrno = newChrno-26 #We account for if we go over z.
   return chr(newChrno) # Return the chr num.
def probs(string): #Make a function that find the probability of each string character
   if ord(string) < 65 or ord(string) > 90:
       return 0
   alphaNo= ord(string) -65 #Get the number of it in the alphabet.
   probability= letterGoodness[alphaNo]
   return float(probability)
def bigFunction(encodedString):
   encodedString= encodedString.upper()
   inputo= encodedString
   goodnessList= []
   wordList= []
   for a in range (0, 26): # Loop around all 26 characters of the alphabet.
      newStr = ''
      probabilityNewStr = 0
      for b in range (0, len(inputo)): #Loop through each character in the input
         newStr= newStr + ChrReplace(inputo[b], a) #We replace each character
         probabilityNewStr= probabilityNewStr + probs(newStr[b]) #find the decimal probability of the entire word
      goodnessList.append(probabilityNewStr)
      wordList.append(newStr)
   biggestProbs= max(goodnessList)
   location= goodnessList.index(biggestProbs)
   bigprobsWord= wordList[location]
   return bigprobsWord
print("The actual word is:", bigFunction(inputo)) #The beginning and the end of all