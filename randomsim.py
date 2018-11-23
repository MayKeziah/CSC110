from random import random, randrange

def main(nrolls):
    n5s = 0
    for i in range(nrolls):
        roll = randrange(1, 7)
        if roll == 5:
            n5s = n5s+1

    print("The probability of getting a five appears to be:\n", n5s/nrolls)
    
def graphrand(nPoints):
    import graphics as g
    Win = g.GraphWin("Random Point Graph", 500, 500)
    for i in range(nPoints):
        randPoint = g.Point(randrange(500), randrange(500))
        randPoint.setFill("Red")
        randPoint.draw(Win)

    Win.getMouse()
    Win.close()
