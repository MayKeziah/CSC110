#Program that reads a text file and reports overall grade % and GPA.
#Works for non-weighted grades
# .txt format: "<assn name> <points earned> <points possible>"
#05/18/18

def main():
    #open file
    date = input("Please enter todays date in format MM/DD/YY:\n")

    INfname = input("Please enter the filename you wish to process:\n")
    infile = open(INfname, "r")

    OUTfname = input("Please enter the file you want to track your progress on:\n")
    outfile = open(OUTfname, "a")
    

    #Variables for loop
    Assns = {}
    scores = []
    OfTot = []

    #read file
    for line in infile:
         entry = line.split()
         Assns[entry[0]] = entry[1:3]
         scores.append(eval(entry[1]))
         OfTot.append(eval(entry[2]))
         
    percent = round((sum(scores)*100)/sum(OfTot), 2)
    points = str(sum(scores))+ "/" + str(sum(OfTot))


    prSt = ("Your grade results from '"+INfname+"' are as follows:\n" +
            "Percent total: "+str(percent)+"%\n" +"Point total: "
            +points+"\n")
    print(prSt)
    print(date+"\n"+prSt, file = outfile)
    print("All data has been saved to '"+OUTfname+"'.")

    infile.close()
    outfile.close()

main()

def unsure():
    GPA = round((percent*0.01)*4.0, 1)
    
    NumGrades = [1.0, 1.2, 1.5, 1.9, 2.2, 2.5, 2.9, 3.2, 3.5, 3.9, 4.1]
    LetGrades = ["F", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A"]
    for i in range(len(NumGrades)):
        if GPA < NumGrades[i]:
            Grade = LetGrades[i]
            break
        else: Grade = "Undefined"
