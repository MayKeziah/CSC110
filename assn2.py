#Keziah May
#04/18/18
#Assignment 2

#This program calculates the average, median, and sum
#of a list containing an odd number of values given in ascending order.

def main():
    print("This program calculates the average, median, and sum of a list.")
    print("Enter values sorted in ascending order from left to right.")
    print()
    
    #Prompt user for how many numbers they will enter into the list.
    #Explain perameters to user.
    n = int(input("How many values will you be entering? This must be an odd number: "))
    
    #Start building a loop to calculate the inputs
    thelist = []
    thesum = 0
    for i in range(n): #for every value entered (n values)
        value = int(input("Please enter a value: "))
        thesum = thesum + value #Calculate the sum
        thelist.append(value) #build a list to find the median
    theavg = thesum/n #Calculate average
    themed = thelist[(n-1)//2] #calculate median

    print()
    print("For the values: ", thelist)
    print("The median =", themed)
    print("The average =", theavg)
    print("The sum =", thesum)
    
 

main()
