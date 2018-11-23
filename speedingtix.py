#Textbook Chapter 7, question 6: Speeding ticket fine

#This program determines whether a speed is legal or
#illegal and prints the result including fine amount if illegal.
def main():
    import math
    #Inputs will be clocked speed (Cspeed) and Speed Limit (Lspeed)

    Lspeed = eval(input("Please enter the speed limit: "))
    Cspeed = eval(input("Please enter the clocked speed: "))

    #Determine whether or not they were within the legal speed
    if Lspeed >= Cspeed:
        #Outputs are either a print statement stating the speed was legal...
        print("The clocked speed is within the legal limit.")
    else:
        fine = 50 + 5 * math.floor((Cspeed-Lspeed)/5)
        if Cspeed >= 90: fine = fine + 200
        #...or a print statement stating the fine amount if illegal
        print("$" + str(fine), "fine.")

main()
