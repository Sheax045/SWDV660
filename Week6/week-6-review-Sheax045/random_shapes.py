from graphics import *
from random import *

def inputInfo():
    outputFileName = input('Enter the drawing file name to create: ')
    numOfShapes = input('Enter the number of shapes to make: ')
    randomShapeLoop(numOfShapes, outputFileName)
    
def outputFileInfo(outputFileName, randomShape):
    outputFile = open( outputFileName, "a" )
    print( randomShape, file=outputFile )
    outputFile.close()

def randomShapeLoop(numOfShapes, outputFileName):
    for i in range(int(numOfShapes)):
        randomCoordinates(randomShape(), randomColor(), outputFileName)
        
def randomShape():
    shape = randrange(1, 3)
    if shape == 1:
        shape = 'circle'
    else:
        shape = 'rectangle'
        
    return shape

def randomColor():
    r = 25
    g = 196
    b = randrange(142, 201)
    color = [r, g, b]
    return color

def randomCoordinates(shape, color, outputFileName):
    if shape == 'circle':
        ptX, ptY = randrange(0, 476), randrange(0, 476)
        radius = randrange(5, 51)
        color = '{0}, {1}, {2}'.format(int(color[0]), int(color[1]), int(color[2]))
        randomShape = '{0}; {1}, {2}; {3}; {4}'.format(shape, ptX, ptY, radius, color)
        
    else:
        ulPtX, ulPtY = randrange(0, 476), randrange(0, 476)
        lrPtX, lrPtY = (ulPtX + randrange(5, 51)), (ulPtY + randrange(5, 101))
        color = '{0}, {1}, {2}'.format(int(color[0]), int(color[1]), int(color[2]))
        randomShape = '{0}; {1}, {2}; {3}, {4}; {5}'.format(shape, ulPtX, ulPtY, lrPtX, lrPtY, color)
    
    outputFileInfo(outputFileName, randomShape)
        
def main():
    inputInfo()
    
main()
 