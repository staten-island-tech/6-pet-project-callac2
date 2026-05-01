
class Pet:
    def __init__(self, name, happy_level, food, play):
        self.name = name
        self.happy_level = happy_level
        self.food = food
        self.play = play

""" 
class Interact:
    def __init__(self, pet, happy_level):
        self.pet = pet
        self.happy_level(item)
        print(self.happy_level)

    def interaction(self, play):
        self.play.append(play)
 """
class Interact:
        def __init__(self, pet, happiness):
            self.pet = pet
            self.happiness = happiness 

        def increase(self, amount):
            self.happiness += amount

        def show_happy_level(self):
          print(f"{self.pet} has {self.happiness}")
Max = Interact("Max", 100)
food = input("Do you want to feed your pet, Max?")
while food == ('Yes'):
    Max.increase(20)
    print(Max.__dict__)
    print("Max's happiness increased 40 points!!!!")
    continue_feeding = input("do you want to keep giving Max food?")    
    if continue_feeding == ('Yes'):
        Max.increase(20)
        print("Yay, Max's happiness raised another 40 points!")
        print(Max.__dict__)

    else:
        print(Max.__dict__)

        print("Okay, Max is done eating now. He is happier!!!!")
        break


      

""" Max = Pet("Max", 1/100, ["blue eyes"])

Max.buy({"title": "Hat", "cuteness": 34})
print(Max.__dict__)


def happy_level():
    if Pet.buy ["Hat"]:
        happy_level += 2

        if Pet.buy ["Food"]:
            happy_level += 5



""" 
