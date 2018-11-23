def main():
    sumtotal = 0
    count = 0
    data = 'yes'
    while data == 'yes':
        number = eval(input("Enter a number: "))

        sumtotal = sumtotal + number
        count = count + 1
        data = input("Do you want to enter another number? yes/no\n")

    print("\nAverage = ", sumtotal/count)

def new():
    print("This program calculates the sum of numbers entered.")
    print("Press the enter key to calculate the sum.")
    
    sumtotal = 0
    count = 0
    
    data = input("Enter a number: \n ")
    while data != "":
        number = int(data)
        sumtotal = sumtotal + number
        data = input(" ")
    print("The sum is:", sumtotal)

#Program to find the average of a series of numbers (one per line) read from a file
def fileloop():
    try:
        #Open file to read
        fname = input("What is the name of the file you would like to open?\n")
        infile = open(fname, "r")

        #Set base for accumulators
        sumtotal = 0
        count = 0

        #Read lines of file until the line is blank using indefinite loop
        line = infile.readline()
        
        while line !="":
            num = eval(line)
            sumtotal = sumtotal + num
            count = count + 1
            line = infile.readline()

        print("\nThe average of the numbers in '" + fname + "' is:", sumtotal/count)
        
        infile.close()

    except:
        print("\nThere appears to be an error with the file '" + fname +
              "':\n***Please check that the file contains only one"
              "\n***number per line and no other characters.\n\n")
        fileloop()
fileloop()
