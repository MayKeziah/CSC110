#Keziah May
#05/16/18
#CSC110
#Assn6

def main():
    print("This program calculates fuel efficiency on a multi-leg journey.\n"
          "It returns the MPG per leg and the MPG overall.\n")
    #get the starting odometer reading
    StartMiles = float(input("\nPlease enter your starting odometer reading:\n"))
    BuildLists(StartMiles)
#A function that uses a sentinel loop to build 2 lists from a users input
    #A list of how much gas has been used
    #A list of odometer readings
def BuildLists(StartMiles):
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

   # return 
            
        
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
