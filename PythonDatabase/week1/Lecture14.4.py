class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):  # z is the name input by the user when instance or object is created
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "So far", self.x)

    def __del__(self):
        print(self.name, "destructed with the end value of ", self.x)

class FootballFan(PartyAnimal): #inherit
    points = 0
    def touchdown(self):
        self.points = self.points +  7
        self.party() #inherit the party()
        print(self.name, "points", self.points)


