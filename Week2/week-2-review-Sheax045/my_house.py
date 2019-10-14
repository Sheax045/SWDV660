import graphics as g

# draw 3 rectangles, 2 lines, 1 circle, 1 text label 
# must have color
# make it interactive on click

win = g.GraphWin("My House", 600, 500)


myHouseRect = g.Rectangle( g.Point( 200, 250 ), g.Point( 400, 450 ) )
myHouseRect.setFill( 'tan' )
myHouseRect.draw( win )


skyLine = g.Rectangle( g.Point( 0, 0), g.Point( 600, 150 ) )
skyLine.setFill( 'sky blue' )
skyLine.setOutline( 'sky blue' )
skyLine.draw( win )

theSun = g.Circle( g.Point( 500, 75 ), 50)
theSun.setFill( 'orange' )
theSun.setOutline( 'orange' )
theSun.draw( win )

centerRoofPoint = g.Point( 300, 150 )
theRoofLeft = g.Line( centerRoofPoint, g.Point( 200, 250 ) )
theRoofLeft.setFill( 'brown' )
theRoofLeft.draw( win )
theRoofRight = g.Line( centerRoofPoint, g.Point( 400, 250 ) )
theRoofRight.setFill( 'brown' )
theRoofRight.draw( win )

mailBoxPole = g.Rectangle( g.Point( 95, 400 ), g.Point( 100, 450 ) )
mailBoxPole.setFill( 'brown' )
mailBoxPole.draw( win )
mailBox = g.Rectangle( g.Point( 50, 370 ), g.Point( 100, 400 ) )
mailBox.setFill( 'forest green')
mailBox.draw( win )

mailBoxMessage = g.Text( g.Point( 75, 385 ), "SHEA" )
mailBoxMessage.draw( win )

win.getMouse()
skyLine.setFill( 'black' )
skyLine.setOutline( 'black' )
win.setBackground( 'black' )
theSun.setFill( 'gray' )
theSun.setOutline( 'gray' )