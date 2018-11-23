class button:
    
    def __init__(self, Win, Label):
        self.win = Win
        self.label = Label

    def activate(self):
        "Sets this button to 'activate'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    
