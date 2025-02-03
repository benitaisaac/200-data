# This is assignment 1
class Admins:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.failures = 0
        self.successes = 0
    def incrementFailtures(self):
        self.failures += 1
    def incrementSuccesses(self):
        self.successes += 1 
    def display(self):
        print(f"Welcome {self.name}.\nYou have got {self.failures} failed attempts and  {self.successes} successful attempts.")

class Electronics:
    def __init__(self, name):
        self.name = name
        self.veryBad = 0
        self.bad = 0
        self.good = 0
        self.veryGood = 0
    def veryBad(self):
        self.verBad += 1
    def bad(self):
        self.bad += 1
    def good(self):
        self.good += 1
    def veryGood(self):
        self.veryGood += 1
    def display(self):
        print(f"Name: {self.name}, Very Bad: {self.veryBad}, Bad: {self.bad}, Good:{self.good}, Very Good:{self.veryGood}")
        

admins = {
    "Isaac": Admins("Isaac", 1),
    "Benita": Admins("Benita", 2),
    "Malar": Admins("Malar", 3),
}



