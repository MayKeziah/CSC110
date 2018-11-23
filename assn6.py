#Write a program that computes the fuel efficiency of a multi-leg journey.
#The program will first prompt for a starting odometer reading and then get
#information about a series of legs.  For each leg, the user enters the current
#odometer reading and the amount of gas used (separated by a space).
#The user signals the end of the trip with a blank line.
#The program should print out the miles per gallon achieved on each leg
#and the total MPG for the trip.

#Keziah May
#05/16/18
#CSC110
#Assn6

def main():
    print("This program calculates fuel efficiency on a multi-leg journey.\n"
          "It returns the MPG per leg and the MPG overall.\n")
    #get the starting odometer reading
    StartMiles = float(input("\nPlease enter your starting odometer reading:\n"))

    #set variables
    GasList = [0]
    MileList = [StartMiles]
    Leg = 1
    prompt = input("Please enter your current odometer reading\n"
                   "and the amount of gas used separated by a space.\n"
                   "When finished, press enter to calculate.\n"
                   "Leg 1: ")
    #Start the sentinel loop for legs
    while prompt != "":
        try:
             #Separate miles traveled and Gas used, Convert to float
            Mi, Gas = prompt.split()
            Mi = float(Mi)
            Gas = float(Gas)
            #Form lists of miles traveled and gas used
            MileList.append(Mi)
            GasList.append(Gas)
            #track legs for user
            Leg = Leg+1
            #Prompt for new leg
            newprompt = "Leg " + str(Leg) + ": "
            prompt = input(newprompt)
        except ValueError:
            print("Oops! Try again!")
            newprompt = "Leg " + str(Leg) + ": "
            prompt = input(newprompt)
            
        
    #Loop through Mile and Gas lists for each leg.
    #Count totals and calc MPG per leg
    GasTotal = 0
    MileTotal = 0
    for i in range(len(GasList)):
        GasTotal = GasTotal + GasList[i]
        MileTotal = MileTotal + MileList[i]
        if i == 0:
            print("\nFuel Efficiency for each leg:")
        #Calculate the MPG for each leg and print it
        else:
            MPG = (MileList[i]-MileList[i-1])/(GasList[i]-GasList[i-1])
            print("For leg "+str(i)+",", MPG, "MPG.")

    #Print total MPG
    TotalMPG = (MileTotal-MileList[0])/GasTotal
    print("\nYour overall fuel efficiency for this trip was",
          round(TotalMPG, 2), "MPG.")


main()
