letterGoodness= [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0402, .0241, .0675, .0751, .0193, .0009, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
#print(letterGoodness) #testing... it's predefined
inputo= str(input("Insert your encoded sentence: "))
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
def characterReturn(newStr, ynList):
    for a in range (0, len(newStr)):
        if ynList[a] == 1: # 1= yes, 0= no (binary)
            letterStr= newStr[a]
            letterStr= letterStr.lower()
            newStr= newStr[0: a] + letterStr + newStr[a+1:len(newStr)]
            continue
    return newStr
def ynLister(string):
    ynList= []
    for a in range (0, len(string)):
        individChr= string[a]
        if individChr.isalpha()== False: ynList.append(0)
        elif individChr.islower() == True: ynList.append(1)
        else: ynList.append(0)
    return ynList
def bigFunction(encodedString):
   ynList= ynLister(encodedString)
   encodedString= encodedString.upper()
   inputo= encodedString
   goodnessList= []
   wordList= []
   shiftList= []
   for a in range (0, 26): # Loop around all 26 characters of the alphabet.
      newStr = ''
      probabilityNewStr = 0
      for b in range (0, len(inputo)): #Loop through each character in the input
         newStr += ChrReplace(inputo[b], a) #We replace each character
         probabilityNewStr= probabilityNewStr + probs(newStr[b]) #find the decimal probability of the entire word
      goodnessList.append(probabilityNewStr)
      wordList.append(newStr)
      shiftList.append(a)
   biggestProbs= max(goodnessList)
   location= goodnessList.index(biggestProbs)
   bigprobsWord= wordList[location]
   confirm = input("Does this decoded word make sense? " + str(bigprobsWord) + " Reply yes/no: ") #Get the user's response
   attempts = 3 #Set the attempts
   Error = False 
   while confirm != "yes" and attempts > 0:
       while confirm == "no" and len(wordList) > 1:
            if Error != True:
                goodnessList.remove(biggestProbs) #Try again. Get the second most-likely word.
                wordList.remove(bigprobsWord)
                biggestProbs= max(goodnessList)
                location= goodnessList.index(biggestProbs)
                bigprobsWord= wordList[location]       
                confirm = input("Does this decoded word make sense?:" + str(bigprobsWord) + "Reply yes/no, or if you would like to see a list of all possibilities, reply \"list\":")
                if confirm == "list" or Error == True:
                    Error = False
                    print(wordList)
                    rightWord= str(input("Which word on the list looks right?"))
                    if Error == True:
                        Error = False
                    try:
                        location= wordList.index(rightWord)
                        bigprobsWord= wordList[location]
                    except ValueError: #We catch any errors if the word they enter is not on the list
                        print("I\'m Sorry, that\'s not in the list. Try again.")
                        Error = True
       if len(wordList) <= 1:
           print("There is only one word left. That has to be it!")
           break                 
       elif confirm == "no": continue
       if confirm != "yes" or confirm != "list" or confirm != "no" or Error == True: attempts -= 1
       if attempts == 0: 
           print("Attempts limit reached.")
           break
       if confirm == "yes" and Error != True: break 
       if Error == True: 
           rightWord= input("I\'m sorry, that\'s not on the list. Write a word that is on the list:")
           continue
       if Error == False and confirm == "no": 
           print("Successfully selected a word that appears on the list! Proceed.")
           break 
       confirm= input("I\'m sorry, that\'s invalid. Try again.")
   shiftValue= shiftList[location]
   goodToGo= False
   limit = 3
   while goodToGo== False and limit > 0:
       askQuestion= str(input("Would you like to know what the shift value was? Reply yes/no. Default value = no:"))
       askQuestion= askQuestion.replace(" ", " ")
       if askQuestion.isalpha() != True:
           print("Did you include any non-alphabetic characters in there? Try again.")
           limit -= 1
           continue
       if askQuestion  == "yes":
           questAnsw= True
           goodToGo= True 
           continue
       elif askQuestion == "no":
           questAnsw= False
           goodToGo= True
       elif askQuestion != "yes" or askQuestion != "no":
           print("That\'s not an option. Try again.")
           limit -= 1
           continue
   if limit == 0:
       questAnsw = False
       print("Attempts limit reached. Value set for \"no\" ")
   if questAnsw== True: print("The shift value was", shiftValue)
   return characterReturn(bigprobsWord, ynList)
print("The actual phrase is:", bigFunction(inputo)) #The beginning and the end of all