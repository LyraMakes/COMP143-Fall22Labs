# # Write a function make_shirt that takes a size and the text of a message that should be printed on the shirt
# # as two parameters. The function should print a sentence summarizing the size of the shirt and the message
# # printed on it. Call the function using positional arguments,
# # such as 'M' and 'Walk a mile in my shoes. You'll end up at the library.'
#
# def make_shirt(size, message):
#     print(f'Created Shirt of size "{size}" with message "{message}"')
#
#
# make_shirt('M', "Walk a mile in my shoes. You'll end up at the library.")
#
#
# # Write a function countToMax that asks the user, "How high would you like to count?"
# # The function should then print a column of numbers starting from 0 and ending at the user-specified number.
# # The function countToMax should perform as follows in the two examples below when called with countToMax(),
# # depending on what the user inputs.
#
# def countToMax():
#     num = int(input("How high would you like to count? "))
#     for i in range(0, num + 1):
#         print(i)
#
#
# countToMax()
#
#
# # Write a function square that takes one parameter side and RETURNS the area of a square with side length side.
# # Call the function with an argument. Wrap a print around the function call, so that the returned area is printed.
#
# def square(side):
#     return side * side # side ** 2
#
#
# print(square(4))
#
#
# print([x for x in range(0, 19, 2)])
#

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Dog(name: \"{self.name}\", age: {self.age})"

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def __str__(self):
        pets = ""
        for pet in self.pets:
            pets += f"{pet}\n"
        return f"{self.name} owns pets:\n{pets}"

    def add_pet(self, pet):
        self.pets.append(pet)


me = Owner("Lyra")
me.add_pet(Dog("Darby", 3))
me.add_pet(Dog("RJ", 2))

print(me)



# mydog = Dog("Darby", 3)
# mydog2 = Dog("Darby", 3)
#
# print(mydog)
# print(mydog2)
# print(mydog == mydog2)




