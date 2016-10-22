shiftvalue= 0
from random import randint
def charactershifter(chrt, shiftvalue):
   No= ord(chrt)
   if No == 32:
      return chr(32)
   No += shiftvalue
   if shiftvalue >=0:
      if No > 90:
         b= (No-65)//26
         No -= (26 * b)
   if shiftvalue < 0:
      if No < 65:
         c= (No-65)//26
         No += (26* c)
   No= chr(No)
   return No
# Code below is the same as in 15 C decode.py. Copy-pasted in fact. Adds more convenience to encoding.
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
def encoder(message, shiftvalue):
   newStr= ''
   ynList= ynLister(message)
   originShiftValue = shiftvalue
   if shiftvalue == "rndm": shiftvalue = randint(0,26)
   elif shiftvalue.isdigit() != True:
         return ("I\'m sorry, that\'s not a valid shift value. Please try another number. The value must be an integer.")
   else:
         shiftvalue= int(shiftvalue)
   for a in range(0, len(message)):
      if message[a].isalpha() == False:
            newStr += message[a]
            continue
      else:
            newChr= charactershifter(message[a], shiftvalue)
            newStr += newChr
   newStr= characterReturn(newStr, ynList)
   if originShiftValue == "rndm":
         yesno= input("Would you like to know the shift value? Reply yes/no. Default value = no:")
         tries = 3
         while yesno != "no" and yesno != "yes" and tries > 0:
               print("Invalid. Try again")
               tries -= 1
               if tries == 0: 
                     print("Attempts limit reached")
                     break
               yesno= input("Would you like to know the shift value? Reply yes/no:")
         if yesno == "yes": print("The shift value was", shiftvalue)
   return newStr
print("The encoded word is:", encoder(input("Insert the word of which you would like to encode:"), input("Enter the shift value of the encoder, or enter \"rndm\" to randomize:")))