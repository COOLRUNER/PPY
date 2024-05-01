class Musician:
    def __init__(self, fName, lName, instrument, role):
        self.fName = fName
        self.lName = lName
        self.instrument = instrument
        self.role = role

    def play(self):
        print(f"{self.fName} {self.lName} plays {self.instrument}")


class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def addMusician(self, musician):
        self.members.append(musician)

    def removeMusician(self, Name):
        for member in self.members:
            if member.fName == Name:
                self.members.remove(member)

    def listMusicians(self):
        for member in self.members:
            print(f"{member.fName} {member.lName} - {member.role}")

    def playMusic(self):
        for member in self.members:
            member.play()



