from graphics import *

def newTreeParts(treePart, x, y):
    newPart = treePart.clone()
    newPart.move(x,y)
    return newPart
    
def drawTree(win):       
    treeTrunk = Rectangle( Point( 55, 275 ), Point( 58, 300 ) )
    drawObjectWithColor( treeTrunk, win, 'brown')

    topTreeBranches = Polygon( Point( 56, 198 ), Point( 30, 223 ), Point( 82, 223 ) )
    drawObjectWithColor( topTreeBranches, win, 'forest green')

    middleTreeBranches = Polygon( Point( 56, 223 ), Point( 25, 250 ), Point( 87 , 250 ) )
    drawObjectWithColor( middleTreeBranches, win, 'forest green')

    bottomTreeBranches = Polygon( Point( 56, 250 ), Point( 20, 275 ), Point( 92 , 275 ) )
    drawObjectWithColor( bottomTreeBranches, win, 'forest green')
    
    x, y = 125, 35
    for i in range(4):
        
        newTreeParts(treeTrunk, x, y).draw(win)
        newTreeParts(topTreeBranches, x, y).draw(win)
        newTreeParts(middleTreeBranches, x, y).draw(win)
        newTreeParts(bottomTreeBranches, x, y).draw(win)
        
        x, y = x + 125, y + 35
        
def drawHouse(win):
    myHouseRect = Rectangle( Point( 200, 250 ), Point( 400, 450 ) )
    drawObjectWithColor( myHouseRect, win, 'tan')
    
    centerRoofPoint = Point( 300, 150 )
    theRoofLeft = Line( centerRoofPoint, Point( 200, 250 ) )
    theRoofRight = Line( centerRoofPoint, Point( 400, 250 ) )

    drawObjectWithColor( theRoofLeft, win, 'brown')
    drawObjectWithColor( theRoofRight, win, 'brown')

def drawSkyLine(win):
    skyLine = Rectangle( Point( 0, 0), Point( 600, 150 ) )
    drawObjectWithColor( skyLine, win, 'sky blue')
    
def drawSun(win):
    theSun = Circle( Point( 500, 75 ), 50)
    drawObjectWithColor( theSun, win, 'orange')

def drawMail(win):
    mailBoxPole = Rectangle( Point( 95, 400 ), Point( 100, 450 ) )
    drawObjectWithColor( mailBoxPole, win, 'brown')
    mailBox = Rectangle( Point( 50, 370 ), Point( 100, 400 ) )
    drawObjectWithColor( mailBox, win, 'forest green')
   
    mailBoxMessage = Text( Point( 75, 385 ), "SHEA" )
    mailBoxMessage.draw( win )

def onClick (win): 
    win.getMouse()
    skyLine = Rectangle( Point( 0, 0), Point( 600, 150 ) )
    drawObjectWithColor( skyLine, win, 'black')
    theSun = Circle( Point( 500, 75 ), 50)
    drawObjectWithColor( theSun, win, 'gray')
    win.setBackground( 'black' )

    
def drawObjectWithColor( objectName, win, color ):
    objectName.setFill( color )
    objectName.setOutline( color )
    objectName.draw( win )
        
def main():
    win = GraphWin("My House", 600, 500)
    
    drawMail(win)
    drawSkyLine(win)
    drawSun(win)
    drawTree(win)
    drawHouse(win)
    
    onClick(win)
         
   
main()


       
 #      newTopTreeBranches = topTreeBranches.clone()
#       newTopTreeBranches.move(125,35)
#       newTopTreeBranches.draw(win)
#       topTreeBranches = newTopTreeBranches
#       newMiddleTreeBranches = middleTreeBranches.clone()
#       newMiddleTreeBranches.move(125,35)
#       newMiddleTreeBranches.draw(win)
#       middleTreeBranches = newMiddleTreeBranches
#       newBottomTreeBranches = bottomTreeBranches.clone()
#       newBottomTreeBranches.move(125,35)
#       newBottomTreeBranches.draw(win)
 #     bottomTreeBranches = newBottomTreeBranches
