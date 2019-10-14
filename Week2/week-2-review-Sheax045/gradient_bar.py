#window must be 400 pixels wide X
#no gaps between rectangles
#bars must be a multiple of 6
#The bars must have no outline (hint: setWidth method)
#All bars must have a width within one pixel of the same width. 

import graphics as g

win = g.GraphWin( "Gradient Bar", 400, 200 )


firstRectangle = g.Rectangle( g.Point( 0, 0 ), g.Point( 66, 200) )
firstRectangle.setWidth(0)
firstRectangle.setFill('#0066ff')
firstRectangle.draw( win )
secondRectangleClone =  firstRectangle.clone()
secondRectangleClone.setFill('#0055c7')
secondRectangleClone.move( 66, 0)
secondRectangleClone.draw( win )

thirdRectangle = g.Rectangle( g.Point( 132, 0 ), g.Point( 199, 200) )
thirdRectangle.setWidth(0)
thirdRectangle.setFill('#004290')
thirdRectangle.draw( win )

moveBar = 67

for barSets in range (3):
    colorList = ['#002e5b', '#0f1a2a', '#000000']
    thirdRectangleClone = thirdRectangle.clone()
    thirdRectangleClone.move( moveBar, 0)
    thirdRectangleClone.setFill(colorList[barSets])
    thirdRectangleClone.setWidth(0)
    thirdRectangleClone.draw( win )
    moveBar = moveBar + 67
 

