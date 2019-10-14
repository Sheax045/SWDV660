#create graphical window
#draw eye in window by making 2 rectangles with one filled as black
#need 5 eyes drawn
#on mouse click move black part of eye to where click was, eyes only move on x axis and never outsite of big rectangle
#when clicked shift most boxes to left/right but if click is in box x axis then the pupil shifts to have the closest leading edge line up with the click point.


from graphics import *

def drawEyes(win):
    upperLeftPointEye = Point(100, 100)
    lowerRightPoint = Point(200,200)
    upperLeftPointPupil = Point(150, 150)
    
    eye = Rectangle(upperLeftPointEye, lowerRightPoint)
    pupil = Rectangle(upperLeftPointPupil, lowerRightPoint)
    
    eye.setOutline('black')
    eye.draw(win)
    pupil.setFill('black')
    pupil.draw(win)
    
    pupilX = lowerRightPoint.getX()
 #can draw all 5 eyes but need to figure out how to make them all move on click   
    for i in range (4):
        newEye = eye.clone()
        newEye.move(125,0)
        newEye.draw(win)
        eye = newEye
        
        newPupil = pupil.clone()
        newPupil.move(125,0)
        newPupil.draw(win)
        pupil = newPupil
 #need to make loop with X points that will work for all pupils       
    while True:
        mouseClick = win.getMouse()
        print(mouseClick.getX())
        
        if mouseClick.getX() >= pupilX:
            if pupilX == 150:
                pupil.move(50, 0)
                pupilX = pupilX + 50              
            else:
                print('hey')               
        else:
            if pupilX == 200:
                pupil.move(-50, 0)
                pupilX = pupilX - 50
 
            else:
                print('no')
 #need to figure out how if click is in width of eye (X) to make eye move to edge of that point      
            
    
    
    
    
def mouseClick(win, pupilX):
    win.getMouse
    return getX(), getY()

def main():
    win = GraphWin("All Eyes on You", 800, 500)
    
    drawEyes(win)
       
    
#need loop that determines if getX() value is greater/less than than current pupil X value.
#if greater move right, if smaller move left or stay in position    
       
        
    
    
    
main()
