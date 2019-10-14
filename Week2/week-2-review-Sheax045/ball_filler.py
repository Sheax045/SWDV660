# calculate the amount of filler the company should order
# V=4/3πr3
# prompt user to input # of balls manufactured
# the diameter of each ball in inches
# volume of the core in inches cubed
# compute and output the amount of filler needed

import math

numberOfBallsManu = input( "How many bowling balls will be manufactured? " )
diameterOfBall = input( "What is the diameter of each ball in inches? " )
coreVolume = input( "What is the core volume in inches cubed? " )

radiusOfBall = float(diameterOfBall) / 2

volumeOfBall = (4/3) *  (math.pi * radiusOfBall**3)
volumeOfBallWithoutCore = volumeOfBall - int(coreVolume)
fillerNeededForAllBalls = volumeOfBallWithoutCore * int(numberOfBallsManu)

print( "You will need " + str(fillerNeededForAllBalls) + " inches cubed of filler")

