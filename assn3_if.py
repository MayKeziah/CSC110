#Keziah May
#04/25/18
#Assignment 3
#CSC110

#This program reads file "scores.dat"
#Prints student name, their number score, and their letter grade
#Saves to a new file, "grades.dat"


def main():
    print("This program identifies a student's final letter grade")
    print("using information from a given file.")
    print()
    iname = input("Which file should I process for you? ")
    print()
    oname = "grades.dat"
    infile = open(iname, "r") #open in-file
    outfile = open(oname, "w") #Open out-file

   
    data = infile.readlines() #Read file
    for line in data:
        first,last,score = line.split() #Split the lines into a list
        score = eval(score)
        if score<60:    grade = "F"
        elif score <70: grade = "D"
        elif score <80: grade = "C"
        elif score <90: grade = "B"
        else:           grade = "A"

        #Write a script for the outfile
        newline = [first, last, "received a score of", str(score), "for a grade of", grade]
        gradeline = " ".join(newline) + "."

        #Print outfile info for user
        print(gradeline)

        #Write outfile script for outfile
        outline = [first, last, str(score)]
        gradeoutscript = " ".join(outline) + " " + grade

        #Write out-script to outfile
        print(gradeoutscript, file=outfile)
        
    print()
    print("This information can now be accessed in the file 'grades.dat'.")

    

    #Close files
    infile.close() 
    outfile.close()
main()
