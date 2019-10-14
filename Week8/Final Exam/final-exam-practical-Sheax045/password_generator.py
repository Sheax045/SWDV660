#generate password from length user inputs
#ask via input how many characters
#use randrange to generate a number and use that number as an index to the alphabet
#print new password
from random import *
class RandomPassword:
    def __init__(self):
        print()
        
    def passwordInput():
           passwordCharInput = int(input( "How many characters for your password? " ))
           return passwordCharInput

    def passwordGenerator(passwordCharInput):
        password = ''
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

        for i in range(passwordCharInput):
            randomCharNum = randrange(0, 52)
            password = password + alphabet[randomCharNum]
    
        print('Your password is: {0}'.format(password))

def main():
    
    RandomPassword.passwordGenerator(RandomPassword.passwordInput())

main()