#Keziah May
#04/24/2018
# UPDATE TO Assignment 1 

#Demonstrate understanding of
#input, process, output using a
#prompt, basic maths, and clear labels

def main():
    try:
        x = int(input("List an integer: "))
        theSquare = Square(x)
        theRecip = Reciprocal(x)
        theSqRc = SquareofRecip(x)
        print("Reciprocal: ", theRecip)
        print("Square: ", theSquare)
        print("The square of the recip: ", theSqRc)
    except ValueError:
        print("\nThis is not an integer. Try again...\n")
        main()
    except ZeroDivisionError:
        print("\nZero is not a valid input. Try again...\n")
        main()
    except:
        print("\nIt looks like an error has occurred.\n"
            "Please check your integer and try again...\n")
        main()            
    
    
def Reciprocal(value):
    return 1/value

def Square(value):
    return value**2

def SquareofRecip(value):
    return Square(Reciprocal(value))

main()


    
