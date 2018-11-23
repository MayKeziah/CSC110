import graphics

#Draw a dot!
def main():
    mypoint = graphics.Point(250, 250)
    mywin = graphics.GraphWin("Test Graphics", 500, 500)
    mypoint.draw(mywin)
    mypoint.setFill("red")
    return mypoint

def circle():
    mywin = graphics.GraphWin("My siiiiiick little circle", 320, 240)
    mycircle = graphics.Circle(graphics.Point(100,100), 50)
    centerpt = mycircle.getCenter()
    mycircle.draw(mywin)
    return mycircle
    
def test():

    mywin = graphics.GraphWin("Test Graphics", 500, 500)
    for i in range(500):
        mypoint = graphics.Point(i, i*3)
        mypoint.draw(mywin)
    return mypoint
