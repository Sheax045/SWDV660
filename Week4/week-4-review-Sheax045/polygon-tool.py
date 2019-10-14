import graphics as g
win = g.GraphWin ( "Polygon Maker", 700, 600 )

quitRec = g.Rectangle(g.Point(25,50), g.Point(100, 100))
quitRec.setFill("Red")
quitRec.setOutline("Red")
quitRec.draw(win)
quitText = g.Text(g.Point(62.5,75), "Quit")
quitText.draw(win)

numOfClicks = 0

clickSeq = []

while True:
    p = win.getMouse()
    clickSeq.append(p)
    numOfClicks = numOfClicks + 1
    if (25 < p.getX() < 100) and (50 < p.getY() < 100):
        point1 = clickSeq[numOfClicks - 2]
        point2 = clickSeq[numOfClicks - numOfClicks]
        line = g.Line(point1, point2)
        line.draw(win)
        break
    elif numOfClicks >= 2:
       for i in range (len(clickSeq)):
           point1 = clickSeq[numOfClicks - 2]
           point2 = clickSeq[numOfClicks - 1]
           line = g.Line(point1, point2)
           line.draw(win)
           break
    else:
        p.draw(win)
            