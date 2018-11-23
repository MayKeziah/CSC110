class student:
    def __init__(self, Firstname, Lastname, Score):
        self.firstname = Firstname
        self.lastname = Lastname
        self.score = float(Score)
        print("New student object created:", self.firstname)
    def getFirstname(self):
        return self.firstname
    def getLastname(self):
        return self.lastname
    def getScore(self):
        return self.score
    def getGrade(self):
        sgrade = ""
        if self.score>=90: sgrade = "A"
        elif self.score>=80: sgrade = "B"
        elif self.score>=70: sgrade = "C"
        elif self.score>=60: sgrade = "D"
        else: sgrade = "F"
        return sgrade
