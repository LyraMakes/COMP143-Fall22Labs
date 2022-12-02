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

