from random import *

def playerInput():
    startMoney = int(input('Enter the number of dollars you start with: '))
    numSpins = int(input('Enter the number of spins you will play: '))
    betAmt = int(input('Enter how many dollars you will bet for each spin: '))
    print('Choose one of the following strategy choices')
    print(' - Bet on a (s)ingle number (pays 35 to 1)')
    print(' - Bet on (e)ven or odd numbers (pays 1 to 1)')
    print(' - Bet on a (d)ozen numbers (pays 2 to 1)')
    print()
    strategyChoice(startMoney, numSpins, betAmt)
    
    
def strategyChoice(startMoney, numSpins, betAmt):
    strategy = input('Enter your strategy choice (s, e, d): ')
    if strategy == 's':
        betChoice = input('Enter the single number you want to bet on (00 or 0 to 36): ')
    elif strategy == 'e':
        betChoice = input('Enter if you want to bet on (e)ven or (o)dd numbers: ')
    else: 
        betChoice = input('Enter 1 to bet on numbers 1-12, 2 for numbers 13-24, or 3 for numbers 25-36: ')
    print()
    winOrLose(startMoney, numSpins, strategy, betChoice, betAmt)
    
#def wheelSpin():
#    randomSpin = randrange(0, 38)
#    return randomSpin
    #37 will be used for 00
    
def winOrLose(startMoney, numSpins, strategy, betChoice, betAmt):
    spinCount = 0
    winCount = 0
    lossCount = 0
   
    winnings = 0
    losses = 0
    totalWinnings = 0
    netWinnings = 0
    totalMoney = startMoney + winnings - losses
    for spin in range (numSpins):
        if totalMoney > 0:
            spinCount = spinCount + 1
            randomSpin = randrange(0, 38)
            if strategy == 's':
                BetSingleNum(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses)
            elif strategy == 'e':
                BetEvenOdd(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses)
            else:
                BetDozen(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses)
            totalWinnings = totalWinnings + winnings
            totalMoney = totalMoney + winnings - losses
            winCount = winCount + winCount
            lossCount = lossCount + lossCount
            losses = losses + losses
    netWinnings = totalWinnings - losses
    results(spinCount,winCount,lossCount,totalMoney,netWinnings)
                
                   
def BetSingleNum(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses):
    if betChoice == 00:
        betChoice = 37
    elif betChoice == randomSpin:
        winnings = betAmt * 35
        winCount = winCount + 1
        return winnings, winCount
    else:
        losses = losses + betAmt
        lossCount = lossCount + 1
        return losses, lossCount
            
def BetEvenOdd(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses, lossCount2):
    if betChoice == 'e':
        if randomSpin % 2 == 0:
            winnings = betAmt * 2
            winCount = winCount + 1
            return winnings, winCount
        else:
            losses = losses + betAmt
            lossCount = lossCount + 1
            return losses, lossCount2
    else:
        if betChoice == 'o':
            if randomSpin == 37:
                losses = losses + betAmt
                lossCount = lossCount + 1
                return losses
            elif randomSpin % 2 == 1:
                winnings = betAmt * 2
                winCount = winCount + 1
            return winnings, winCount
        else:
            losses = losses + betAmt
            lossCount = lossCount + 1
            return losses, lossCount 
    
def BetDozen(betChoice, randomSpin, betAmt, winCount, lossCount, winnings, losses):
    firstDozen = (1,2,3,4,5,6,7,8,9,10,11,12)
    secondDozen = (13,14,15,16,17,18,19,20,21,22,23,24)
    thirdDozen = (25,26,27,28,29,30,31,32,33,34,35,36)
    if betChoice == 1 and randomSpin in firstDozen:
        winnings = betAmt + (betAmt * 2)
        winCount = winCount + 1
        return winnings,  winCount
    elif betChoice == 2 and randomSpin in secondDozen:
        winnings = betAmt + (betAmt * 2)
        winCount = winCount + 1
        return winnings, winCount
    elif betChoice == 3 and randomSpin in thirdDozen:
        winnings = betAmt + (betAmt * 2)
        winCount = winCount + 1
        return winnings, winCount
    else:
        losses = losses + betAmt
        lossCount = lossCount + 1
        return losses, lossCount
            

def results(spinCount,winCount,lossCount,totalMoney,netWinnings):
    try:
        print('After {0} spins'.format(spinCount))
        print('Wins: {0} ({1}%)'.format(winCount, winCount/spinCount))
        print('Losses: {0} ({1}%)'.format(lossCount, (lossCount/spinCount)))
        print('Ending bank: ${0}'.format(totalMoney))
        print('Net winnings: ${0}'.format(netWinnings))
    except ZeroDivisionError as error:
        print('Wins: 0 0%')
        
def main():
   playerInput()
    
  

main()