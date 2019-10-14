from graphics import *
from button import Button
from die_view import DieView

class SumCounterView:
    dieCount = 0
    def __init__( self, dieRoll1Value, dieRoll2Value, win ):
        self.dieRoll1Value = dieRoll1Value
        self.dieRoll2Value = dieRoll2Value
        self.dieSum = self.dieRoll1Value + self.dieRoll2Value
        self.dieCount = dieCount

        
        if self.dieSum == 4:
            
            ptY1, ptY2, ptY3 = 25, 50, 38
            self.countMessage(ptY1, ptY2, ptY3, self.dieSum, self.handleRoll( self.dieSum ), win)
        
        elif self.dieSum == 5:
            
            ptY1, ptY2, ptY3 = 65, 90, 78
            self.countMessage(ptY1, ptY2, ptY3, self.dieSum, self.handleRoll( self.dieSum ), win)

 
        elif self.dieSum == 6:
            
            ptY1, ptY2, ptY3 = 105, 130, 118
            self.countMessage(ptY1, ptY2, ptY3, self.dieSum, self.handleRoll( self.dieSum ), win)
            
        elif self.dieSum == 7:
            
            ptY1, ptY2, ptY3 = 145, 170, 158
            self.countMessage(ptY1, ptY2, ptY3, self.dieSum, self.handleRoll( self.dieSum ), win)
 
    def countMessage(self, ptY1, ptY2, ptY3, dieSum, dieCount, win):
        self.textRect = Rectangle( Point(210, ptY1), Point(385, ptY2))
        self.textRect.setFill( 'white' )
        self.message = Text(Point(295, ptY3), "Total of {0} counted {1} times".format(self.dieSum, self.dieCount))
        self.textRect.draw( win )
        self.message.draw(win)
        
    
    def handleRoll( self, dieSum ):
        if self.dieSum == 4:
            self.dieCount += 1
            return self.dieCount
        elif self.dieSum == 5:
            self.dieCount += 1
            return self.dieCount
        elif self.dieSum == 6:
            self.dieCount += 1
            return self.dieCount
        elif self.dieSum == 7:
            self.dieCount += 1
            return self.dieCount