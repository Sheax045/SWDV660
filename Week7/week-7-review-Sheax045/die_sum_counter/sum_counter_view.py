from graphics import *
from button import Button
from die_view import DieView

dieCountSumFour = 0
dieCountSumFive = 0
dieCountSumSix = 0 
dieCountSumSeven = 0 

class SumCounterView:
    
    def __init__( self, dieCountSum,  win):
        global dieCountSumFour
        global dieCountSumFive
        global dieCountSumSix
        global dieCountSumSeven
        
        if dieCountSum == 4:
            dieCountSumFour = dieCountSumFour + 1
            self.countMessage(25, 50, 38, 4, dieCountSumFour, win)
        elif dieCountSum == 5:
            dieCountSumFive = dieCountSumFive + 1
            self.countMessage(65, 90, 78, 5, dieCountSumFive, win)
        elif dieCountSum == 6:
            dieCountSumSix = dieCountSumSix + 1
            self.countMessage(105, 130, 118, 6, dieCountSumSix, win)
        elif dieCountSum == 7:
            dieCountSumSeven = dieCountSumSeven + 1
            self.countMessage(145, 170, 158, 7, dieCountSumSeven, win)                                    
        
    def countMessage(self, ptY1, ptY2, ptY3, dieSum, dieCount, win):
        self.dieSum  = dieSum
        
        self.textRect = Rectangle( Point(210, ptY1), Point(385, ptY2))
        self.textRect.setFill( 'white' )
        self.message = Text(Point(295, ptY3), "Total of {0} counted {1} times".format(dieSum, dieCount))
        self.textRect.draw( win )
        self.message.draw(win)
    
    def handleRoll( self, dieSum ):
        
        
 