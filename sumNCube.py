#Keziah May
#In-Class 04/26
#CSC110

#A Function that prints the sum of the first 'n' natural numbers and
##the sum of the cubes of the first 'n' natural numbers
def main():
    print("This program calculates the sum of the first natural numbers within")
    print("a given range as well as the sum of the cubes of those same numbers.")
    print()
    n = int(input("Please enter a positive integer to set the range: "))
    print()
    print("The sum of the first", n, "natural numbers is: ", sumN(n))
    print("The sum of the cubes of the first", n,
          "natural numbers is: ", sumNCubes(n))

#Returns the sum of the first 'n' natural numbers
def sumN(n): 
    theSum = 0 #Accumultor Variable
    for i in list(range(n)):
        theSum = theSum+i
    return theSum

#Returns the sum of the cubes of the first 'n' natural numbers
def sumNCubes(n): 
    theSumNCube = 0 #Accumultor Variable
    for i in list(range(n)):
        theSumNCube = theSumNCube + (i**3)
    return theSumNCube

main()
