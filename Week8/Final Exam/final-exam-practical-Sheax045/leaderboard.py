#process file with video game scores from file scores.txt
#loop thru the lines and seperate on the ','
#determine what is easy, med, and hard and determine high score of each
#once a score is higher than last, save score and name associated.
#output the highest score and name for each difficulty level 

def highScore(scoreLines, difficultyLevel ):
    #setting variables to determine highest score for each difficulty level
    highestScore = 0
    
 #looping thru the lines to determine which score is the highest for each difficulty level
    for i in range(len(scoreLines)):
        playerInfo = scoreLines[i].split(',')
        if playerInfo[1] == difficultyLevel:
            if int(playerInfo[2]) > highestScore:
                highestScore = int(playerInfo[2])
                playerName = playerInfo[0]
                
    return playerName, highestScore


def main():
    #opening file to read
    scoresList = open( 'scores.txt', 'r' )
    scoreLines = scoresList.readlines()
    
                
                
 #output information for highest scores for all difficulty levels
    print('********** LEADERBOARD **********')
     
    print('{0:6} : {1} with {2} points'.format('Easy',highScore(scoreLines, 'Easy')[0], highScore(scoreLines, 'Easy')[1]))
    
    print('{0} : {1} with {2} points'.format('Medium', highScore(scoreLines, 'Med')[0], highScore(scoreLines, 'Med')[1]))

    print('{0:6} : {1} with {2} points'.format('Hard',  highScore(scoreLines, 'Hard')[0],  highScore(scoreLines, 'Hard')[1]))

main()
