#Assignment_3 Batch-Oriented Program

def main():
    # filenames
    infileName = input("Enter a .dat file: ")
    #outfileName = "scores.dat"

    # open files
    infile = open(infileName, "r")
   # outfile = open(outfileName, "w")

    # process each line 
    for line in infile:

        # get the first and last names and also the score from line
        first, last, score = line.split()

        # converts the scores
        index = int(score)/10

        # grades list used as a look up table
        Grade = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

        # get the letter grade 
        grade = Grade[int(index)]


        # create string with all the information
        student = (first + " " + last + " " + "receives a score of" + " " + score + " " + "for a grade of" + " " + grade + ".\n")
 
        # write the output to our file
        #print(student, file=outfile)

        print(student)

    # close both files
    infile.close()
    #outfile.close()

    print("New file have been written to", outfileName)


