
def welcomeAndMenu():
    computeShape = "{0}   Compute area of a {1}"
    print("Welcome to the area computation tool!\n")
    print("****** MENU ******")
    print(computeShape.format('tri ', 'triangle'))
    print(computeShape.format('trap', 'trapezoid'))
    print(computeShape.format('pent', 'pentagon'))
    print("{0}   Quit the tool\n".format('quit'))
    
def userInput():
    choiceInput = input("Please enter your choice: ")
    while choiceInput not in ('tri', 'trap', 'pent', 'quit'):
        print("'{0}' is an invalid choice".format(choiceInput))
        choiceInput = input("Please enter your choice: ")
    return choiceInput


def main():
    welcomeAndMenu()
    print("You chose: ", userInput())
    
main()

