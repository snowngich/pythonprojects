class Dog:
    # Constructor method to initialize object attributes
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute

    # Method that makes the dog bark
    def bark(self):
        print(f"{self.name} is barking!")
my_dog=Dog("buddy","white") # Creating an instance of Dog
print(my_dog.name)  # Accessing object attribute
my_dog.bark()  # Calling object method
