from button import Button
from die_view import DieView
from graphics import *
from sum_counter_view import SumCounterView

def main():
    win = GraphWin("Double Die Roller", 400, 200)
    win.setBackground( 'dark green' )
    dieView1 = DieView( win, Point( 50, 60 ), 80 )
    dieView2 = DieView( win, Point( 150, 60 ), 80 )
    rollButton = Button( win, Point( 100, 160), 100, 40, "Roll!" )
    
    while True:
        mouseClick = win.getMouse()
        if rollButton.wasClickedIn( mouseClick ):
            dieRoll1Value = dieView1.roll()
            dieRoll2Value = dieView2.roll()
            SumCounterView(dieCountSum, win)
        
            #SumCounterView( 4, dieRoll1Value, dieRoll2Value, win, 25, 50, 38)
            #SumCounterView( 5, dieRoll1Value, dieRoll2Value, win, 65, 90, 78 )
            #SumCounterView( 6, dieRoll1Value, dieRoll2Value, win, 105, 130, 118 )
            #SumCounterView( 7, dieRoll1Value, dieRoll2Value, win, 145, 170, 158 )
    
main()