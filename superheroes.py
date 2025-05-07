# In this python program we will work on classess and objects

#TASK 1. Let's create a class -> superhero
#DEFINE A CLASS

# Define the Superhero class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name        # Superhero's name
        self.power = power      # SuperStrengh
        self.origin = origin    # Origin 

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")
