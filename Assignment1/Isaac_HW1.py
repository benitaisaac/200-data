# This is assignment 1
successLogins = 0
failedLogins = 0
class Admins:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Welcome {self.name}.\nThere have been {failedLogins} failed attempts and {successLogins} successful logins.")

class Electronics:
    def __init__(self, name):
        self.name = name
        self.veryBad = 0
        self.bad = 0
        self.good = 0
        self.veryGood = 0
    def fveryBad(self):
        self.veryBad += 1
    def fbad(self):
        self.bad += 1
    def fgood(self):
        self.good += 1
    def fveryGood(self):
        self.veryGood += 1
    def display(self):
        print(f"Name: {self.name}, Very Bad: {self.veryBad}, Bad: {self.bad}, Good:{self.good}, Very Good:{self.veryGood}")
        

admins = {
    "1": Admins("Isaac", 1),
    "2": Admins("Benita", 2),
    "3": Admins("Malar", 3),
}

electronics = [
    Electronics("SamSung TV",),
    Electronics("Hitachi Remote",),
]

def processAdmin():
    global successLogins
    global failedLogins
    id = input("Enter your ID ")
    #if id in [x.id for x in admins.values()]
    if id not in admins.keys():
        failedLogins += 1
        return
    successLogins += 1
    admins[id].display()
    for x in electronics:
        x.display()
    yn = input(f"Do you want to add/delete electronics? a(add)/d(delete) ")
    if yn not in ["a", "d"]:
        return
    if yn == "a":
        en = input(f"Enter your electronic name ")
        electronics.append(Electronics(en))
    else:
        en = input(f"Enter the electronic name you want to delete. \n{[x.name for x in electronics]} ")
        for e in electronics: 
            if e.name == en:
                electronics.remove(e)

def processCustomer():
    for e in electronics:
        print(f"name={e.name}")
    electronicName = input("Enter a name from above ")
    if electronicName not in [e.name for e in electronics]:
        print(f"Bad value {electronicName}")
        return
    rating = input(f"Enter your rating. \n 1 = Very Bad, 2 = Bad, 3 = Good, 4 = Very Good ")
    if rating not in ["1", "2", "3", "4"]:
        print(f"Please enter a valid value")
        return
    for e in electronics:
        if e.name == electronicName:
            myelectronics = e
            break
    
    if rating == "1":
        myelectronics.fveryBad()
    elif rating == "2":
        myelectronics.fbad()
    elif rating == "3":
        myelectronics.fgood()
    elif rating == "4":
        myelectronics.fveryGood()



def main():
    while True:
        au = input("""
          1. Admin
          2. User
    Your Choice: """)
        if au in ["1", "2"]:
            break
        print(f"Invalid input {au}.")
    if au == "1":
        processAdmin()
    else:
        processCustomer()


if __name__ == "__main__":
   while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n exiting")
            break
