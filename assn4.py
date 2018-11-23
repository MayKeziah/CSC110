#Keziah May
#05/04/18
#Assignment 4
#CSC110

######QUESTION TO DR.BODINE! Does this need to write to a file? question source(rubric)
#This is a program that computes
#the sum of the squares of numbers read from a file.

def main():
    #Explain the program function and parameters to the user
    print("This program computes the sum of the")
    print("squares of numbers read from a file.")
    print()
    print("NOTE: This file must be formatted such that")
    print("each number is entered on a separate line.")
    print()

    #Open file to read
    fname = input("Which file would you like me to process for you? ")
    print()
    infile = open(fname, "r")
    
    #Read File
    strList = infile.readlines()
    for line in range(len(strList)):
        strList[line] = strList[line].rstrip() #Remove '\n' from each index

    #process file
    nums = toNumbers(strList) #convert string list to number list
    squares = squareEach(nums) #convert number list to squares of number list
    thesum = sumList(squares) #Find sum of squares of number list

    #Give result to user
    print("The sum of the squares of the numbers")
    print("provided in the file \"" + fname + "\" is: ",thesum)
    
    #Close file
    infile.close()

#A function that modifies a list (nums) of numbers by squaring each entry.
def squareEach(nums): 
    for i in range(len(nums)):
        nums[i] = nums[i]**2 #modify list
    return nums #return modified list

#A function that retutns the sum of a list (nums) of numbers.
def sumList(nums):
    thesum = 0
    for i in nums:
        thesum = i + thesum #Add values
    return thesum #Return final sum

#A function that modifies a list (strList) of strings
#(that represent numbers) into the same list of numbers.
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = eval(strList[i])
    return strList
    
main()
