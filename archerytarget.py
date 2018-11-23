import graphics
#draw archery rings
def main():
    #Set window dimentions

    WinDim = eval(input("Enter the desired dimentions of the square window (ex. 200):\n"))
    mywin = graphics.GraphWin("Archery Target", WinDim, WinDim)

    #Circles
    center = graphics.Point((WinDim-1)/2,(WinDim-1)/2)

    #Set width of rings/radius of bullseye
    width = WinDim/10
    circles = []
    colors = ["white", "black", "blue", "red", "yellow"]
    for i in range(5):
        circle = graphics.Circle(center, width*(5-i))
        circles.append(circle)
        circle.draw(mywin)
        circle.setFill(colors[i])

main()
