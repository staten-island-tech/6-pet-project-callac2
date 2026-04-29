
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
            self.happiness = happiness  # double underscore means "private"

        def increase(self, amount):
            self.happiness += amount

        def show_happy_level(self):
          print(f"{self.pet} has {self.happiness}")
Max = Interact("Max", 100)
Max.increase(12)

print(Max.__dict__)
      

""" Max = Pet("Max", 1/100, ["blue eyes"])

Max.buy({"title": "Hat", "cuteness": 34})
print(Max.__dict__)


def happy_level():
    if Pet.buy ["Hat"]:
        happy_level += 2

        if Pet.buy ["Food"]:
            happy_level += 5



""" ''' class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
Bob = BankAccount("Bob", 100)
Bob.deposit(12)

print(Bob.__dict__) """