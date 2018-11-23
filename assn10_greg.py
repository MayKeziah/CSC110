#This is a random walk simulator.  It will step a particle "n" number of times in a random direction.
#Each step will be the same distance.
#By Greg Eggenberger


import graphics
import math
import random


def main():
    n = int(input("Please input the number of steps. ", ))
    mywin = graphics.GraphWin("Random Walk",500,500)
    mywin.setCoords(-50,-50,50,50)
    x = 0
    y = 0

    for i in range(n):
        p1 = graphics.Point(x,y)
        angle = random.random()*2*math.pi
        x,y = getPoint(x,y,angle)
        p2 = graphics.Point(x,y)
        myline = getLine(p1,p2)
        myline.draw(mywin)
        

def getPoint(x,y,angle):
    x = x + math.cos(angle)
    y = y + math.sin(angle)
    return x,y

def getLine(p1,p2):
    myline = graphics.Line(p1,p2)
    return myline


main()
