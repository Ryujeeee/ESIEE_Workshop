# In this python program we will work on classess and objects

#TASK 1. Let's create a class -> superhero
#DEFINE A CLASS

# Define the Superhero class
class Superhero:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self.power = power

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")
        
#TASK 2. ADD POWER AND FRIENDS ATTRIBUTES

# Define the Superhero class with powers and friends attributes
class Superhero:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self.powers = []
        self.friends = []

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Origin: {self.origin}")
        print("Powers:")
        for power in self.powers:
            print(f"  - {power}")
        print("Friends:")
        for friend in self.friends:
            print(f"  - {friend}")


#TASK 3. Add methods for use of 5 superpowers (minimum). Method must initialize a superpower


class Superhero:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin
        self.powers = []
        self.friends = []

    def add_power(self, power):
        if power not in self.powers:
            self.powers.append(power)

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Origin: {self.origin}")
        print("Powers:")
        for power in self.powers:
            print(f"  - {power}")
        print("Friends:")
        for friend in self.friends:
            print(f"  - {friend}")

    # ----- Superpower Methods -----
    def fly(self):
        self.add_power("Flight")
        print(f"{self.name} takes off into the sky with incredible speed!")

    def turn_invisible(self):
        self.add_power("Invisibility")
        print(f"{self.name} fades from sight and becomes completely invisible.")

    def super_strength(self):
        self.add_power("Super Strength")
        print(f"{self.name} lifts a car effortlessly with immense strength!")

    def teleport(self):
        self.add_power("Teleportation")
        print(f"{self.name} vanishes and reappears miles away in a blink!")

    def shoot_lasers(self):
        self.add_power("Laser Vision")
        print(f"{self.name} shoots blazing lasers from their eyes!")


# Create Superman
superman = Superhero("Superman", "Planet Krypton")

# Add friends
superman.add_friend("Batman")
superman.add_friend("Catwoman")
superman.add_friend("Sentry")

# Use superpowers
superman.fly()
superman.super_strength()
superman.shoot_lasers()
superman.turn_invisible()
superman.teleport()

# Display Superman's details
superman.display_info()




