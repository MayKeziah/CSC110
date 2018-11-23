
#A program to determine how long it will take for an investment to double
def main():
    intrate = float(input("What is the annual interest rate? (ex. 2.3)\n")) * 0.01
    investment = 100
    double = 200
    years = 0
    while investment < double:
        investment = investment + investment * intrate
        years = years + 1
        
    print("Your investment will double in", years, "years.")
    

#main()

def factor():
    x = eval(input("Please enter an integer: "))
    n = x

    facts = []
    while n > 0:
        if x%n == 0:
            facts.append(n)
            n = n-1
        else:
            n = n-1

    if len(facts) == 2:
        print("'" + str(x) + "' is a prime number.")

    else:
        print("The factors of '" + str(x) + "' are:")
        for i in facts:
            print (i, end=",")

factor()
