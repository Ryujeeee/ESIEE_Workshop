# In this python program we will work on classess and objects

#TASK 1. Let's create a class -> superhero
#DEFINE A CLASS

# Define the Superhero class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = Sentry        # Sentry
        self.power = SuperStrengh      # SuperStrengh
        self.origin = France    # Origin 

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")
        
#TASK 2. ADD POWER AND FRIENDS ATTRIBUTES

# Define the Superhero class with powers and friends attributes
class Superhero:
    def __init__(self, name, origin):
        self.name = Sentry               # Superhero's name
        self.origin = France           # Origin or backstory
        self.powers = [SuperStrengh,Fly,FireResistence]   # List to store multiple powers
        self.friends = [Ghost,Falcons]              # List to store names of friends

    def add_power(self, power):
        self.powers.append(power)      # Add a power to the list

    def add_friend(self, friend_name):
        self.friends.append(friend_name)  # Add a friend's name to the list

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Origin: {self.origin}")
        print("Powers:")
        for power in self.powers:
            print(f"  - {power}")
        print("Friends:")
        for friend in self.friends:
            print(f"  - {friend}")

