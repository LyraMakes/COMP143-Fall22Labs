# from dogutils import Dog, DogOwner


# characteristics - name, age
# behaviors - sit, roll over


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} sat down!")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def __str__(self):
        return f"Dog(name=\"{self.name}\", age=\"{self.age}\")"


    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# You will create objects based on the classes (using the __init__ method)
myDog = Dog("Luna", 4)
myDog2 = Dog("Luna", 4)

print(myDog)
print(myDog2)

print(myDog == myDog2)
print(myDog.__eq__(myDog2))

# "type" keyword clarifications:
# print(type("Content"))
# print(type(myDog))


# You will modify the attributes of an object,
# like updating the age of a dog named Luna,
# directly and through methods.
# print(myDog.age)
# myDog.age = 5
# print(myDog.age)


# You will call methods on objects,
# such as calling the roll_over method on a dog Luna.
# myDog.sit()
# myDog.roll_over()


# You may use instances of one class as attributes in another class.
# owner class could have as an attribute a list of dog objects

class DogOwner:
    def __init__(self, name):
        self.name = name
        self.dogs = []

    def adopt(self, dog):
        self.dogs.append(dog)
        print(f"{self.name} just adopted {dog.name}!")


    def show_dogs(self):
        print(f"{self.name} owns:")
        for dog in self.dogs:
            print(f"{dog.name}, age: {dog.age}")

    def __str__(self):
        return f"DogOwner(name=\"{self.name}\", len(dogs)={len(self.dogs)})"


myOwner = DogOwner("Lyra")
myOwner.adopt(Dog("Darby", 4))
myOwner.adopt(Dog("RJ", 2))

myOwner.show_dogs()

print(f"Dog owner: {myOwner.name}")

print(myDog)
print(myOwner)
