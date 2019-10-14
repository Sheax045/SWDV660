daysOfScores = input( "How many days of scores? " )
totalScore = 0

for dailyRatings in range (int(daysOfScores)):
    dailyScore = input( "Enter score for day " + str(dailyRatings + 1) + ": " )
    totalScore = totalScore + int( dailyScore )  

print( "The total score of the " + daysOfScores + " days is " + str(totalScore) )