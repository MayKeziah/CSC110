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

    #Generate list of letters
    letters = "F "*60 + "D "*10 + "C "*10 + "B "*10 + "A "*10
    LetterList = letters.split()
   
    data = infile.readlines() #Read file
    for line in data:
        first,last,score = line.split() #Split the lines into a list

        #Translate score into index of LetterList
        Grade = LetterList[eval(score)]

        #Write a script for the outfile
        newline = [first, last, "received a score of", score, "for a grade of", Grade]
        gradeline = " ".join(newline) + "."

        #Print outfile info for user
        print(gradeline)

        #Write outfile script for outfile
        outline = [first, last, score]
        gradeoutscript = " ".join(outline) + " " + Grade

        #Write out-script to outfile
        print(gradeoutscript, file=outfile)
        
    print()
    print("This information can now be accessed in the file 'grades.dat'.")

    

    #Close files
    infile.close() 
    outfile.close()
#main()

#This program finds the average of a set of scores
#and then identifies how far above/below average
#each student scored
def dataedit():
    #readfile
    fname = input("Enter the filename:\n")
    infile = open(fname, "r")

    #Empty lists
    scorelist = []
    firstnamelist = []
    lastnamelist = []
    
    #put data in list
    for line in infile:
        first, last, score = line.split()
        score = int(score)
        scorelist.append(score)
        firstnamelist.append(first)
        lastnamelist.append(last)

    #Find the average: accumulator loop
    tally = 0
    counts = 0

    for i in scorelist:
        tally = tally + i
        counts = counts + 1

    average = tally/counts

    #Loop over data again, comparing each score
    for i in range(len(scorelist)):
        points = "points"
        if scorelist[i] > average:
            diff = scorelist[i]-average
            up_down = "above average."
        elif scorelist[i] < average:
            diff = average-scorelist[i]
            up_down = "below average."
        else:
            diff = ""
            up_down = "average"
            points = ""

        print(firstnamelist[i], lastnamelist[i], "scored", scorelist[i], ",", diff, points, up_down)

    infile.close()

#dataedit()
    
def dictname():
    #readfile
    fname = input("Enter the filename:\n")
    infile = open(fname, "r")

    #Variables
    StudGrad = {}
    scores = []
  
    #Loop for data storage
    for line in infile:
        entry = line.split()
        StudGrad[entry[1]+","+entry[0]]=eval(entry[2])
        scores.append(eval(entry[2]))   
    average = sum(scores)/len(scores)
    print()
    #Find relitive avg
    for student in StudGrad:
        points = "points"
        if StudGrad[student] > average:
            diff = StudGrad[student]-average
            up_down = "above average."
        elif StudGrad[student] < average:
            diff = average-StudGrad[student]
            up_down = "below average."
        else:
            diff = ""
            up_down = "average"
            points = ""
        print(student, "received a score of ", StudGrad[student], end = ".\n")
        print("This score is", diff, points, up_down, "\n")

    infile.close()

dictname()
