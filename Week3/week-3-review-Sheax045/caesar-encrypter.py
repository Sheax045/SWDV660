inputFile = input("Enter the input file name: ")
inputMessage = open(inputFile, "r")
key = int( input("Enter the shift key: " ))
outputFileName = input("Enter the output file name: " )
message = inputMessage.read()

    
alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

#print( alphabet )
#print( shiftedAlphabet )

encryptedMessage = ""

for character in message:
    
    letterIndex = alphabet.find( character )
    encryptedCharacter = shiftedAlphabet[letterIndex]
    #print( "{0} -> {1}".format( character, encryptedCharacter ) )
    
    encryptedMessage = encryptedMessage + encryptedCharacter
    
splitMessage = encryptedMessage.split("s")

newEncryptedMessage = ""

for i in range(len(splitMessage) - 1):
    stripMessage = splitMessage[i].strip()
    newEncryptedMessage = newEncryptedMessage + stripMessage + "\n"

lastEncryptedMessage = newEncryptedMessage.strip()

print( "The encrypted message is: {0}".format( lastEncryptedMessage ))

outputFile = open( outputFileName, "w" )
print( lastEncryptedMessage, file=outputFile )
outputFile.close()

print( "Done writing encrypted message to file {0}".format( outputFileName) )
