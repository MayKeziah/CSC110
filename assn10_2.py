#ASSIGNMENT 10 NO. 2

import graphics as g
import random as r
import math as m

def main():
    win = createWin() #Create Win, rtn win
    win.setBackground("lightgrey")
    #A person takes a walk of len(input), the walk is traced
    takeAwalk(Walker(getInput(win), g.Point(50, 50), win))
    

############################################################
##CLASS#####################################################
############################################################

class Walker:
    def __init__(self, stepCount, locationPoint, window):
        self.stepCount = stepCount
        self.location = locationPoint
        self.window = window
    def getWindow(self):
        return self.window
    def getStepCount(self):
        return self.stepCount
    def getLocation(self):
        return self.location
    
    def takeStep(self): #Rtn new location (one step in random direction)
        degree = r.randrange(360)
        angle = (degree*m.pi)/180
        x = (self.location).getX() + m.cos(angle)
        y = (self.location).getY()+ m.sin(angle)
        self.location = g.Point(x, y)
        return self.location
    def drawLocation(self): #Draw blue point at current location
        point = self.location
        point.setFill("blue")
        point.draw(self.window)
    def drawStep(self, point1, point2): #trace step
        line = g.Line(point1, point2)
        line.setOutline("red")
        line.draw(self.window)
    def xMarks(self): #Draw 'x'(for start&end walk)
        theSpot = g.Text(self.location, "x")
        theSpot.setStyle("bold")
        theSpot.draw(self.window)
        
############################################################
##OPERATIONS################################################
############################################################
    
def createWin(): #Create the window
    win = g.GraphWin("Walking Simulation", 800, 800)
    win.setCoords(0, 0, 100, 100)
    grid(win)
    return win

def grid(window): #draw a grid
    for gridline in range(1, 100):
        x = g.Line(g.Point(gridline, 0), g.Point(gridline, 100))
        y = g.Line(g.Point(0, gridline), g.Point(100, gridline))
        for z in [x, y]:
            z.setFill("gainsboro")
            z.draw(window)

def getInput(win): #Get the number of steps for this walk
    message = g.Text(g.Point(50, 54),"How many steps"+
                     " would you like to take?")
    message.draw(win)
    input = g.Entry(g.Point(46, 50), 5)
    input.setText("0")
    input.draw(win)
    rect = g.Rectangle(g.Point(51.5,51.5), g.Point(56.5,48.5))
    rect.setFill("green3")
    rect.setOutline("lightgreen")
    rect.draw(win)
    button = g.Text(g.Point(54, 50),"Walk")
    button.draw(win)
    win.getMouse()
    steps = ""
    while type(steps) != int:
        try:
            steps = int(input.getText())
        except ValueError:
            message.setText("ERROR:"+
                            "The number of steps must be an integer.\n"+
                        "Try again...")
            message.setFill("red")
            win.getMouse()
            steps = ""
        
    for z in [input, rect, button, message]:
        z.undraw()
    return steps

def takeAwalk(person): #Walk N steps, trace walk, quit
    person.xMarks()
    for steps in range(person.getStepCount()):
        person.drawStep(person.getLocation(), person.takeStep())
        person.drawLocation()
    person.xMarks()
    closeMe(person)
    
def closeMe(person): #Close Win
    message = g.Text(g.Point(50, 75), "Click to Quit")
    message.setStyle("bold")
    message.draw(person.getWindow())
    person.getWindow().getMouse()
    person.getWindow().close()

main()
