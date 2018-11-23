#Keziah May
#05/09/18
#CSC110
#Assignment 5

#Objective: demonstrate exception handling and decision structures statements

#This program determines a students class level using their earned credits
def main():
    try:
        print("\nThis Program identifies your class standing given your total credits earned.")
        Ncredits = float(input("Please enter the number of credits earned: "))

        #Determine their class level
        #0-6 freshman, 7-15 sophomore, 16-25 junior, 26+ senior
        if 0 <= Ncredits < 7:
            student = "freshman"
        elif 7 <= Ncredits < 16:
            student = "sophomore"
        elif 16 <= Ncredits < 26:
            student = "junior"
        elif Ncredits > 26:
            student = "senior"

        #Print class level to user
        print("\nYou are a " + student + ".")

    #Handle errors, loop back to main()
    except ValueError:
        print("\nYour entry does not appear to be a number, please try again..\n")
        main()
    except UnboundLocalError:
        print("\nYour entry must be larger than zero, please try again..\n")
        main()
    except:
        print("\nAn unexpected error has occured, please try again..\n")
        main()
        
        
main()


    

