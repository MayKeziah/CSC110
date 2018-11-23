#Keziah May
#04/17/18
#In class activity: Week 3

#Goal: prove understanding of splitting strings

def main():
    #Explain the goal of the program
    print("This program demonstrates splitting strings.\n")

    #Assign string to variable "mystring". 
    mystring = 'This is a line.\n This is a separate line.'
    print("Before: ")
    print(mystring)

    #Split variable mystring into two strings
    mysplit = mystring.split(".\n ")
    print("After: ")
    print(mysplit)
    

    #Assign new string to variable "mystring"
    mystring = 'this_is_a_line.'
    print("Before: ")
    print(mystring)

    #Split variable "mystring" into separate strings of words
    mysplit = mystring.split("_")
    print("After: ")
    print(mysplit)

main()
