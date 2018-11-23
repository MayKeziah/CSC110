
#A program to loop over text files and return the number of names on each line

def main():
    #Explain what the program does
    print("This program reads a text file.\n"
          "The number of names on each line will be printed to the screen.\n")

    #Get file name and then open it
    fname = input("Enter the filename you would like to process:\n")
    infile = open(fname, "r")

    #implement for loop
    for line in infile:
        #split names at comma
        numbers = line.split(",")

        #use a counting loop
        count = 0
        for n in numbers:
            count += eval(n)

        #print the result of counting loop
        print("The sum for this line is", count)

    infile.close()
main()
