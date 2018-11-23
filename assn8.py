#Keziah May
#05/28/18
#CSC110
#Assignment 8

#Super class for all person types
class Person:
    def __init__(self, relationship, name):
        self.Relationship = relationship
        self.Name = name
        
    def SetRelationship(self, NewRelationship):
        self.Relationship = NewRelationship
    def GetRelationship(self):
        return self.Relationship
    
    def SetName(self, NewName):
        self.Name = NewName
    def GetName(self):
        return self.Name
    
        
#Class for customers and Business partners
class Separate(Person):
    def __init__(self, relationship, name, businessname, responsibleemployee):
        Person.__init__(self, relationship, name)
        self.BusinessName = businessname
        self.ResponsibleEmployee = responsibleemployee

    def SetBusinessName(self, NewBusinessName):
        self.BusinessName = NewBusinessName
    def GetBusinessName(self):
        return self.BusinessName

    def SetResponsibleEmployee(self, NewResponsibleEmployee):
        self.ResponsibleEmployee = NewResponsibleEmployee
    def GetResponsibleEmployee(self):
        return self.ResponsibleEmployee

#Class for Employees
class Employee(Person):
    def __init__(self, relationship, name, title, dept, boss, salary, startdate):
        Person.__init__(self, relationship, name)
        self.Title = title
        self.Dept = dept
        self.Boss = boss
        self.Salary = salary
        self.StartDate = startdate
        
    def SetTitle(self, NewTitle):
        self.Title = NewTitle
    def GetTitle(self):
        return self.Title

    def SetDept(self, NewDept):
        self.Dept = NewDept
    def GetDept(self):
        return self.Dept

    def SetBoss(self, NewBoss):
        self.Boss = NewBoss
    def GetBoss(self):
        return self.boss

    def SetSalary(self, NewSalary):
        self.Salary = NewSalary
    def GetSalary(self):
        return self.Salary

    def SetStartDate(self, NewStartDate):
        self.StartDate = NewStartDate
    def GetStartDate(self):
        return self.StartDate

#Class for Customers
class Customer(Separate):
    def __init__(self, relationship, name, businessname, responsibleemployee, accountnum, accountsize):
        Separate.__init__(self, relationship, name, businessname, responsibleemployee)
        self.AccountNum = accountnum
        self.AccountSize = accountsize

    def SetAccountNum(self, NewAccountNum):
        self.AccountNum = NewAccountNum
    def GetAccountNum(self):
        return self.AccountNum

    def SetAccountSize(self, NewAccountSize):
        self.AccountSize = NewAccountSize
    def GetAccountSize(self):
        return self.AccountSize

#Class for Business Partners
class BusinessPartner(Separate):
    def __init__(self, relationship, name, businessname, responsibleemployee, businesstype):
        Separate.__init__(self, relationship, name, businessname, responsibleemployee)
        self.BusinessType = businesstype

    def SetBusinessType(self, NewBusinessType):
        self.BusinessType = NewBusinessType
    def GetBusinessType(self):
        return self.BusinessType

#A function that reads a file of a list of people and sorts them into separate lists
#based on class.
#Returns a list of people where each person has a type.
def main():
    #Open and read file
    fname = input("Please enter the name of the file you would like to process:\n")
    infile = open(fname, "r")


    #Create a list of 'people strings' from file
    people = infile.readlines()
    
    people.sort() #Sort people by type and name

    #Assign sorted people a type
    for i in range(len(people)):
        people[i] = people[i].split(", ")
        people[i][len(people[i])-1] = people[i][len(people[i])-1].rstrip()

        if "Employee" in people[i]:
            people[i] = Employee(people[i][0], people[i][1], people[i][2], people[i][3],
                           people[i][4], people[i][5], people[i][6])
            
        elif "Customer" in people[i]:
            people[i] = Customer(people[i][0], people[i][1], people[i][2], people[i][3],
                            people[i][4], people[i][5])

        elif "Business Partner" in people[i]:
            people[i] = BusinessPartner(people[i][0], people[i][1], people[i][2], people[i][3],
                                     people[i][4])

    #Return list of people (with defined classes)
    print("The list of people from '"+fname+"' have been saved to your chosen list name.")
    return people

    #Close file
    infile.close()

#A function to explain to user how to use program
def ExplainProgram():
    print("This program takes information about business partners,\n"
          "customers, and employees read from a file, and\n"
          "stores said information to be accessed and edited.\n"
          "\nHow to use this program:\n"
          "\nYou will be asked to input the file you want to process,\n"
          "so be sure to have its name handy.\n"
          "Choose a name (<PeopleList>) to be associated with the people from the file.\n"
          "Each person will be represented by an index of <PeopleList>.\n"
          "Example:\n"
          "   Person1 = PeopleList[index]\n"
          "\n\nWhen you are ready to begin, type the following:\n"
          "   <PeopleList> = main() \n"
          'Replace "<PeopleList>" with any suitable name.')

ExplainProgram()          
          

