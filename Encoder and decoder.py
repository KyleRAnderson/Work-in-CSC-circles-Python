end = ""
tries = 4
encodeValue = 0
decodeValue= 0
while end != "end" and tries > 0:
    userFeedback= input("Would you like to encode something or decode something? Reply with \"decode\" or \"encode\"")
    while ((userFeedback != "encode") and (userFeedback != "decode")) and tries > 0:
        tries -= 1
        if tries != 1: print("I'm sorry, that is not a valid choice. You have", tries, "tries left.")
        else: print("I'm sorry, that is not a valid choice. You have", tries, "try left.") 
        if tries != 0:
            userFeedback= input("Would you like to encode something or decode something? Reply with \"decode\" or \"encode\"")
    if userFeedback == "decode": 
         print("Entering decoding program...")
         if decodeValue > 0:importlib.reload(decoder)
         elif decodeValue == 0 : import decoder
         print("Exiting decoding program...")
    elif userFeedback == "encode":
         print("Entering encoding program...")
         if encodeValue > 0:importlib.reload(Encoder)
         elif encodeValue == 0 : import Encoder
         print("Exiting encoding program...")
    if tries == 0: 
        print("To retry, restart the program manually...")
        break
    end = input("Would you like to restart the program? Reply \"end\" to end the program. Anything else will restart.")
    if end != "end":
        tries= 4
        import importlib
        if userFeedback == "encode": encodeValue += 1
        if userFeedback == "decode": decodeValue += 1   
print("Program terminated...")