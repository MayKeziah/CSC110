#Keziah May
#06/13/18
#CSC110
#Assignment 10

import graphics as g
import random as r
import math as m



def main():
    #Open Win
    goal = "Walking Simulation"
    pixeldimension = 800
    coordmin = 0
    coordmax = 100
    mywin = makewin(goal, pixeldimension, coordmin, coordmax)

    #Draw grid
    grid(coordmax, mywin)

    #Set walker location
    WalkerStart = g.Point(coordmax/2, coordmax/2)
    walkerdraw(WalkerStart, mywin)
    xMarks(WalkerStart, mywin)

    #Input steps
    stepNum = getInput(WalkerStart.getX(), WalkerStart.getY()+2, 3, mywin)

    #Go for a walk
    for count in range(stepNum):
        end = step(WalkerStart)
        goWalk(WalkerStart, end, mywin)
        WalkerStart = end
    xMarks(WalkerStart, mywin)

    #Close Win
    g.Text(g.Point(50, 75), "Click to Quit").draw(mywin)
    mywin.getMouse()
    mywin.close()

    

#Marks the spot with an x provided a point and a window
def xMarks(theSpot, win):
    point = g.Text(theSpot, "x")
    point.draw(win)
    point.setStyle("bold")
#A program that takes input (number of steps) from a user and returns it
def getInput(x, y, width, win):
    message = g.Text(g.Point(x, y+4),"How many steps"+
                     " would you like to take?")
    message.draw(win)
    input = g.Entry(g.Point(x-4, y), width)
    input.setText("0")
    input.draw(win)
    rect = g.Rectangle(g.Point(x+1.5,y+1.5), g.Point(x+6.5,y-1.5))
    rect.setFill("green3")
    rect.setOutline("lightgreen")
    rect.draw(win)
    button = g.Text(g.Point(x+4, y),"Walk")
    button.draw(win)
    win.getMouse()
    steps = int(input.getText())
    for z in [input, rect, button, message]:
        z.undraw()
    return steps

#Make a window
def makewin(goal, dimensions, coordmin, coordmax):
    win = g.GraphWin(goal, dimensions, dimensions)
    win.setCoords(coordmin, coordmin, coordmax, coordmax)
    return win

#A program that draws a grid using the coordinate max of a given square window
def grid(lines, win):
    for gridline in range(1, lines):
        x = g.Line(g.Point(gridline, 0), g.Point(gridline, 100))
        y = g.Line(g.Point(0, gridline), g.Point(100, gridline))
        for z in [x, y]:
            z.setFill("gainsboro")
            z.draw(win)

#Draw the location of the walker with a given point and window
def walkerdraw(walker, win):
    walker.setOutline("blue")
    walker.draw(win)

#draws step-line and end point of walker
def goWalk(start, end, win):
    walkerdraw(end, win)
    drawline(start, end, win)
    
    
#A program that takes a walkers location
#and returns the coords of their next random location
def step(point1):
    degree = r.randrange(360)
    angle = (degree*m.pi)/180
    x = point1.getX() + m.cos(angle)
    y = point1.getY()+ m.sin(angle)
    return g.Point(x, y)

#A program that draws a line given two points and a window
def drawline(point1, point2, win):
    line = g.Line(point1, point2)
    line.setOutline("red")
    line.draw(win)
        
main()
