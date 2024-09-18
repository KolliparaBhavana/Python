class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."

# Creating an object (instance of the class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Fork", 4)
dog3 = Dog("lolo", 5)
print(dog1.name,dog1.description())
print(dog2.name,dog2.description())
print(dog3.name,dog3.description())
dogs=[dog1,dog2,dog3]
from functools import reduce
age_sum=reduce(lambda x,dogs:x+dogs.age,dogs,0)
print(age_sum)


