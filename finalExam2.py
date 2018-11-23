##FINAL--FIXED
from graphics import *

class Face:
    def __init__(self, win, point):
        self.HeadR = 50
        self.EyeR = 10 #EDIT
        self.HalfNose = 5 #EDIT
        self.thrqrt = (self.HeadR*3)/8
        self.window = win
        self.head = Circle(point, self.HeadR)
        self.head.setFill("yellow")
        self.eye1 = Circle(Point(point.getX()-self.thrqrt, point.getY()+self.thrqrt), self.EyeR)
        self.eye2 = self.eye1.clone()
        self.eye2.move(self.thrqrt*2, 0)
        for elt in [self.eye1, self.eye2]:
            elt.setFill("blue")
        self.nose = Rectangle(Point(point.getX()+self.HalfNose, point.getY()-self.thrqrt+self.HalfNose),#EDIT
                              Point(point.getX()-self.HalfNose, point.getY()-self.thrqrt-self.HalfNose))#EDIT
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
    def setEyeSize(self, radius):
        self.EyeR = radius
    def setNoseSize(self, width):
        self.HalfNose = float(width)/2
            

def main():
    mywin = makeWin()
    intro(mywin)
    makeAface(mywin)
    close(mywin)

def makeAface(win):
    message = Text(Point(0, 480), "Click anywhere to Draw a custom face")#EDIT
    message.draw(win)
    yourface = Face(win, win.getMouse())
    message.undraw()
    colorFace(win, yourface)#EDIT
    featureSize(win, yourface)#EDIT
    yourface.drawFace() #EDIT

def featureSize(win, yourface):
    yourface.setHeadSize(getNewSize(win, "head", "radius"))
    yourface.setEyeSize(getNewSize(win, "eye", "radius"))
    yourface.setNoseSize(getNewSize(win, "nose", "width"))

def getNewSize(win, FacePart, requestType):
    message = Text(Point(0, 490), "Enter the "+FacePart + requestType+". Click to enter or to skip.")
    message.draw(win)
    input = Entry(Point(0, 460), 10)
    input.setText(requestType)
    input.draw(win)
    win.getMouse()
    NewSize = input.getText()
    if NewSize == requestType:#EDIT
        if "h" in FacePart:
            NewSize = 50
        elif ("y" or "n") in FacePart:
            NewSize = 10
    message.undraw()
    input.undraw()
    return NewSize

def colorFace(win, yourface):#EDIT
    yourface.setHeadFill(getFill(win, "head"))
    yourface.setEyeFill(getFill(win, "eye"))
    yourface.setNoseFill(getFill(win, "nose"))

def getFill(win, FacePart):
    message = Text(Point(0, 490), "Enter the "+FacePart+" color. Click to enter or to skip.")
    message.draw(win)
    input = Entry(Point(0, 460), 10)
    input.setText("Color")
    input.draw(win)
    win.getMouse()
    NewFill = input.getText()
    if NewFill == "Color":#EDIT
        NewFill = "white"
    message.undraw()
    input.undraw()
    return NewFill
    
    

def close(win):
    win.getMouse()#EDIT
    win.close()#EDIT

def makeWin():
    mywin = GraphWin("Faces!", 800, 800)
    mywin.setCoords(-500, -500, 500, 500)
    return mywin
    
def intro(win):
    message = Text(Point(0, 0), "Click anywhere to start")#EDIT
    message.draw(win)#EDIT
    myface = Face(win, win.getMouse())
    myface.drawFace()
    message.setText("Click again for another face example")#EDIT
    myface2 = UniqueFace(Face(win, win.getMouse()), "blue", "red", "yellow")
    message.undraw()#EDIT
    myface2.drawFace()


def UniqueFace(Face, headFill, eyeFill, noseFill):
    Face.setHeadFill(headFill)
    Face.setEyeFill(eyeFill)
    Face.setNoseFill(noseFill)
    return Face


main()
                              
                                    

