class PartyAnimal:
    x = 0
    def __init__(self):
        print('I;m constructed')

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print("I.m destructed with the end value of ", self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print("Now an contains", an)


class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):  # z is the name input by the user when instance or object is created
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "So far", self.x)

    def __del__(self):
        print(self.name, "destructed with the end value of ", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
j.party()