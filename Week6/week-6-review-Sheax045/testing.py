from random import *

def introAndInput():
    print('This program rolls two 6-sided dice until their sum is a given target value.')
    targetSum = input('Enter the target sum to roll for: ')
    #added a loop so no number lower than 2 or higher than 12 can be entered
    while int(targetSum) < 2 or int(targetSum) > 12:
        targetSum = input('Enter the target sum to roll for: ')
    print()
    return targetSum
    
        
def diceRoll(targetSum):
    rollCount = 0
    diceSum = 0
    while diceSum != int(targetSum):
        randomDiceRoll1 = randrange(1,7)
        randomDiceRoll2 = randrange(1,7)
        diceSum = randomDiceRoll1 + randomDiceRoll2
        rollCount = rollCount + 1
        print('Roll: {0} and {1}, sum is {2}'.format(randomDiceRoll1, randomDiceRoll2, diceSum))
    if diceSum == int(targetSum):
        print('Got it in {0} rolls!'.format(rollCount))
          
          
def main():
    diceRoll(introAndInput())
          

main()