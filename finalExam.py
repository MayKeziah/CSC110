##FINAL##
from graphics import *

class Face:
    def __init__(self, win, point):
        self.HeadR = 50
        self.thrqrt = (self.HeadR*3)/8
        self.window = win
        self.head = Circle(point, self.HeadR)
        self.head.setFill("yellow")
        self.eye1 = Circle(Point(point.getX()-self.thrqrt, point.getY()+self.thrqrt), 10)
        self.eye2 = self.eye1.clone()
        self.eye2.move(self.thrqrt*2, 0)
        for elt in [self.eye1, self.eye2]:
            elt.setFill("blue")
        self.nose = Rectangle(Point(point.getX()+5, point.getY()-self.thrqrt+5),
                              Point(point.getX()-5, point.getY()-self.thrqrt-5))
        self.nose.setFill("red")
        self.mouth = Line(Point(point.getX()-self.thrqrt, point.getY()-(self.thrqrt*2)),
                          Point(point.getX()+self.thrqrt, point.getY()-(self.thrqrt*2)))
        
    def drawFace(self):
        for elt in [self.head, self.eye1, self.eye2, self.nose, self.mouth]:
            elt.draw(self.window)

    def setHeadFill(self, color):
        self.head.setFill(color)

    def setEyeFill(self, color):
        self.eye1.setFill(color)
        self.eye2.setFill(color)

    def setNoseFill(self, color):
        self.nose.setFill(color)

    def setHeadSize(self, radius):
        self.HeadR = radius
            

def main():
    mywin = makeWin()
    intro(mywin)
    makeAface(mywin)
    close(mywin)

def makeAface(win):
    message = Text(Point(0, 480), "Click anywhere to Draw a face")
    message.draw(win)
    yourface = Face(win, win.getMouse())
    message.undraw()
    yourface.setHeadFill(getFill(win, "head"))
    yourface.setEyeFill(getFill(win, "eye"))
    yourface.setNoseFill(getFill(win, "nose"))
    yourface.draw(win)


def getFill(win, FacePart):
    message = Text(Point(0, 490), "Enter the "+FacePart+" color. Click to enter or to skip.")
    message.draw(win)
    input = Entry(Point(0, 460), 10)
    input.setText("Color")
    input.draw(win)
    win.getMouse()
    NewFill = input.getText()
    message.undraw()
    input.undraw()
    return NewFill
    
    

def close(win):
    mywin.getMouse()
    mywin.close()

def makeWin():
    mywin = GraphWin("Faces!", 800, 800)
    mywin.setCoords(-500, -500, 500, 500)
    return mywin
    
def intro(win):
    myface = Face(win, win.getMouse())
    myface.drawFace()
    myface2 = UniqueFace(Face(win, win.getMouse()), "blue", "red", "yellow")
    myface2.drawFace()


def UniqueFace(Face, headFill, eyeFill, noseFill):
    Face.setHeadFill(headFill)
    Face.setEyeFill(eyeFill)
    Face.setNoseFill(noseFill)
    return Face


main()
                              
                                    
