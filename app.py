class Pet:
    def __init__(self, name, happy_level, food, play):
        self.name = name
        self.happy_level = happy_level
        self.food = food
        self.play = play

    def buy(self, item):
        self.happy_level.append(item)
        print(self.happy_level)

    def interaction(self, play, food):
        self.play.append(play)
        self.food.append(food)

Max = Pet("Max", 1/100, ["blue eyes"])

Max.buy({"title": "Hat", "cuteness": 34})
print(Max.__dict__)

""" 
def happy_level(): """
""" if Pet.buy ["Hat"]:
        happy_level += 2

        if Pet.buy ["Food"]:
            happy_level += 5

 """
