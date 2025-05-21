#Create a class for platypus and its features using multi-level inheritance
# Base class
class Animal:
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def eat(self):
        print(f"The {self.species} is eating.")

    def sleep(self):
        print(f"The {self.species} is sleeping.")


# Intermediate class (inherits from Animal)
class Mammal(Animal):
    def __init__(self, species, color, has_fur, is_warm_blooded):
        super().__init__(species, color)
        self.has_fur = has_fur
        self.is_warm_blooded = is_warm_blooded

# Derived class (inherits from Mammal)
class Platypus(Mammal):
    def __init__(self, color, has_fur, is_warm_blooded, lays_eggs):
        super().__init__("Platypus", color, has_fur, is_warm_blooded)
        self.lays_eggs = lays_eggs

    def swim(self):
        print("The platypus is swimming.")

    def lay_eggs(self):
        if self.lays_eggs:
            print("The platypus lays eggs.")
        else:
            print("This platypus does not lay eggs.")


# Create an object of Platypus
perry = Platypus(color="Brown", has_fur=True, is_warm_blooded=True, lays_eggs=True)

# Accessing methods and properties
print(f"Species: {perry.species}")
print(f"Color: {perry.color}")
print(f"Has Fur: {perry.has_fur}")
print(f"Warm-blooded: {perry.is_warm_blooded}")
print(f"Lays Eggs: {perry.lays_eggs}")

# Call methods
perry.eat()
perry.sleep()
perry.lay_eggs()
perry.swim()


#2Create abstract methods for platypus class
from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, species, color):
        self.species = species
        self.color = color

    def sleep(self):
        print(f"The {self.species} is sleeping.")

    @abstractmethod
    def eat(self):
        pass  # Must be implemented by subclasses


# Abstract subclass of Animal
class Mammal(Animal):
    def __init__(self, species, color, has_fur, is_warm_blooded):
        super().__init__(species, color)
        self.has_fur = has_fur
        self.is_warm_blooded = is_warm_blooded

    @abstractmethod
    def give_birth(self):
        pass  # To be defined by Platypus (special case)


# Concrete subclass of Mammal
class Platypus(Mammal):
    def __init__(self, color, has_fur, is_warm_blooded, lays_eggs, has_bill):
        super().__init__("Platypus", color, has_fur, is_warm_blooded)
        self.lays_eggs = lays_eggs
        self.has_bill = has_bill

    # Implement abstract methods
    def eat(self):
        print("The platypus eats insects and small aquatic animals.")

    def give_birth(self):
        print("The platypus lays eggs instead of giving birth to live young.")

    # Additional methods
    def swim(self):
        print("The platypus is swimming.")

    def detect_prey(self):
        print("The platypus uses electroreception to detect prey.")


# Create an instance of Platypus
perry = Platypus(color="Brown", has_fur=True, is_warm_blooded=True, lays_eggs=True, has_bill=True)

# Access methods
perry.eat()
perry.sleep()
perry.give_birth()
perry.swim()
perry.detect_prey()
