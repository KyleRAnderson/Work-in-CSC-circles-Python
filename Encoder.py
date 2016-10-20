shiftvalue= 0
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
def encoder(message, shiftvalue):
   newStr= ''
   for a in range(0, len(message)):
      newChr= charactershifter(message[a], shiftvalue)
      newStr += newChr
   return newStr
print(encoder('GFABUM UE ZAF M DQMX BXMOQ', -27000))