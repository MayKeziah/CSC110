#Keziah May
#04/18/18
#Assignment 2

#This program calculates the average, median, and sum
#of a list containing an odd number of values given in ascending order.

def main():
    import math #NEW: I added import math so that I could change the median formula
    print("This program calculates the average, median, and sum of a list.")
    
    #Prompt user for how many numbers they will enter into the list.
    #Explain perameters to user.
    n = int(input("How many values will you be entering? This must be an odd number: "))
    
    #Prompt user for list
    mynumbers = eval(input("Enter your numbers in ascending order separated by a comma: "))

    #Find the median
    themedian = mynumbers[math.floor(n/2)] #NEW: changed "int" to "math.floor" for use w/negative values

    #Find the the sum
    thesum = 0
    for i in mynumbers:
        thesum = thesum + i

    #Find the average
    theavg = thesum/n

    #Print results
    print("The median: ", themedian)
    print("The average: ", theavg)
    print("The sum: ", thesum)
 

main()

