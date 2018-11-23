# class level assignment script
#CSC 110 Week 5, Lecture 1
def Level(Ncredits):
    classlevel = "None"
    if Ncredits<45:
        classlevel = "Freshman"
    elif 45<=Ncredits<90:
        classlevel = "Sophomore"
    elif 90<=Ncredits<136:
        classlevel = "Junior"
    elif Ncredits>134:
        classlevel = "Senior"
    #Write the rest of the code needed to classify each student
    print("Student is a",classlevel)
    
