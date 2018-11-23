class Dog:
    def __init__(self, Name, Color, Size):
        self.name = Name
        self.color = Color
        self.size = Size

    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def getSize(self):
        return self.size
    def setSize(self, NewSize):
        self.size = NewSize

#########################################################################
def main():
    dogInfo = input("Enter the dogs name, color, and weight in pounds"+
                    " from the last appointment separated by a comma:\n")
    dogInfo = dogInfo.split(", ")
    aDog = Dog(dogInfo[0], dogInfo[1], dogInfo[2])
    newWeight = input("What is the dogs weight in pounds today?\n")
    print(aDog.getName()+" is a "+aDog.getColor()+" dog.\n"+aDog.getName()+
          "'s weight has increased by", eval(newWeight)-eval(aDog.getSize()), "lbs.")
    aDog.setSize(newWeight)
main()
