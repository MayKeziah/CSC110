#Keziah May
#06/06/18
#CSC110
#Assignment 9

#This is an interactive program that draws a circle and a
#horizontal line and finds their intersection points.
    
from graphics import *
def main():
    import math

    #Make Window
    mywin = GraphWin("New Window", 800, 800)
    mywin.setCoords(-10, -10, 10 , 10)

    #Explain program
    Message = Text(Point(5, 9.5), "This Program draws a circle, a horizontal line,\n"
                   "and reports their intersection points")
    Message.draw(mywin)
    direction = Text(Point(-5, 9.5), "Click to set the radius of your circle")
    direction.draw(mywin)    
    #Make graph
    Yax = Line(Point(0, 10), Point(0, -10))
    Xax = Line(Point(-10, 0), Point(10, 0))
    Yax.setWidth(3)
    Xax.setWidth(3)
    Y_Axis = Yax.draw(mywin)
    X_Axis = Xax.draw(mywin)
    for value in range(-10, 11):
        Hori_line = Line(Point(-10, value), Point(10, value)).draw(mywin)
        Verti_line = Line(Point(value, -10), Point(value, 9)).draw(mywin)
    
    #getMouse for circle radius
    Rpt1 = mywin.getMouse()
    dx = 0-Rpt1.getX()
    dy = 0-Rpt1.getY()
    radius = math.sqrt(dx**2+dy**2)
    
    #Draw circle with given radius at (0,0) in {x, -10, 10}{y, -10, 10} win
    mycircle = Circle(Point(0, 0), radius)
    mycircle.draw(mywin)
    mycircle.setOutline("gold")
    mycircle.setWidth(2)
    direction.undraw()
    
    #gettext for y-int of line in win
    Text(Point(-8, 9.5), "Enter a Y-intercept:").draw(mywin)
    input = Entry(Point(-5.5,9.5), 5)
    input.setText("0")
    input.draw(mywin)
    rectangle = Rectangle(Point(-3.3, 9.3), Point(-4.7, 9.7))
    rectangle.draw(mywin)
    rectangle.setFill("gainsboro")
    button = Text(Point(-4, 9.5), "Submit")
    button.draw(mywin)
    mywin.getMouse()
    
    #Draw line
    Y = eval(input.getText())
    myline = Line(Point(-10, Y), Point(10, Y))
    myline.draw(mywin)
    myline.setOutline("blue")
    myline.setWidth(2)
    
    #Draw intersection points in red
    try:
        XInterCoord = math.sqrt(radius**2-Y**2)
        interPoint1 = Point(-XInterCoord, Y)
        interPoint1.draw(mywin)
        interPoint1.setFill("red")
        interPoint2 = interPoint1.clone()
        interPoint2.move(2*XInterCoord, 0)
        interPoint2.draw(mywin)

        #Print coordinates of intersections if any 
        Coords = ("Coordinates of intersection points:\n"+
              "("+str(round(XInterCoord, 2))+", "+str(Y)+"), ("
             +str(round(-XInterCoord, 2))+", "+str(Y)+")")
        print(Coords)
        Message.setText(Coords)
    except ValueError:
        Text(Point(-7, 8.5), "No points of intersection found").draw(mywin)
        print("No points of intersection found")
    rectangle.setFill("Pink")
    button.setText("Quit")    

    #Close window
    mywin.getMouse()
    mywin.close()
    
main()
