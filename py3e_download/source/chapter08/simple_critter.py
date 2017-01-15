# Simple Critter
# Demonstrates a basic class and object 

class Critter(object):
    """A virtual pet"""
    total=0
    def __init__(self, name):
        self.name=name
        Critter. total +=1
        
    def __str__(self):
        return self.name

    def name(self):
        return (self.name.upper())

    def talk(self):
        print("Hi.  I'm an instance of class Critter and my name is: ",  self.name.upper())

def number():
    print("There are now: ",  Critter.total,  "Critters")
    return


# main
crit1 = Critter("Robin")
number()
crit2 = Critter("Pam")
number()
crit3 = Critter("Belinda")
number()
names = (crit1,  crit2,  crit3)
for thing in names:
    print (thing)
    print ("The name of ", thing,    "is ",  thing.name)

input("\n\nPress the enter key to exit.")

