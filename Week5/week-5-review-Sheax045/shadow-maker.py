from graphics import *

def makeShadow(shape):
    shadow = shape.clone()
    shadow.move(4,4)
    shadow.setFill('light gray')
    shadow.setOutline('light gray')
    
    return shadow

def testShadowMaker():
    win = GraphWin()

    c = Circle( Point( 40, 75 ), 30 )
    c.setOutline( 'blue' )
    c.setFill( 'blue' )

    r = Rectangle( Point( 80, 30 ), Point( 140, 140 ))
    r.setFill( 'orange' )
    r.setOutline( 'orange' )

    makeShadow(c).draw(win)
    makeShadow(r).draw(win)
 
    c.draw( win )
    r.draw( win )
    
    
testShadowMaker()


