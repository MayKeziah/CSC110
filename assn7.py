#Keziah May
#05/23/18
#CSC110
#Assignment 7

#This program takes an integer, "n" 
#The primes less than or equal to n
#are returned in a list and printed to the screen
def main():
    #What do I do?
    print("This program finds all the prime numbers less than\n"
          "or equal to a given number.")
    n = int(input("Please enter a positive integer:\n"))

    #Calculate using algorithm
    primes = Eratosthenes(n)

    #print the primes
    for i in primes:
        print(i, "is a prime number.")

    return primes


#A program that uses the sieve of Eratosthenes to find all the primes
#less than or equal to a given number
def Eratosthenes(n):
    #create list and accumulator variables
    theList = list(range(2, n+1))
    primes = []
    
    while len(theList) > 0: 
        currPrime = theList.pop(0) #pop the current prime
        primes.append(currPrime) #update primes list
        nonPrimes = []

        #Test to see is any values in list are multiples of current prime
        for i in range(len(theList)): 
            if theList[i]%currPrime == 0:
                nonPrimes.append(theList[i])

        #remove list of all non-prime numbers from list
        for i in range(len(nonPrimes)):
            theList.remove(nonPrimes[i])
                      
    return primes
    

main()
