import graphics as g

inputMessage = input("Enter a message: ")
yCoordinates = []
for char in range(len(inputMessage)):
    ordValues = ord(inputMessage[char])
    yCoordinates.append(ordValues)
    
    #print(ordValues)
    
#print(yCoordinates)

win = g.GraphWin("Dynamic Typography Image", 400, 200)
win.setBackground("red")

xCoordinate = 10

for index in range(len(yCoordinates)):
    message = g.Text( g.Point( int(xCoordinate), int(yCoordinates[index]) ), inputMessage[index] )
    #the ordinal value of the letter is being used for the Y axis
    if index % 2 == 0:
        message.setOutline("yellow")
        message.setFace("courier")
    else:
        message.setOutline("blue")
        message.setSize(int(int(yCoordinates[index])/4))
        #in the line above the ordinal value of the letter is being divided by 4 to get the size used for the letter
    message.draw(win)
    xCoordinate = xCoordinate + 15
