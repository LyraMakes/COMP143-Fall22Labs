
# User input
# Write a Python program that prompts the user with
# "How many pounds of coffee do you want to order? "
# and calculates the cost of the order to be shipped from 1369 Coffee House.
# The shop charges $1.50 in overhead costs per order and sells the coffee for $10.50
# a pound plus the cost of shipping. Each order ships for $0.86 per pound.
# State the total cost to the customer using appropriate formatting,
# including rounding the price to two decimal digits (up to the penny).

# pounds = float(input("How many pounds of coffee do you want to order? "))
# total = 1.50 + (10.50 + 0.86) * pounds
# total = round(total, 2)
# print(f"Your total comes to ${total}")
# print(f"This would get you {pounds * 30} cups of coffee")



# While
# Write a Python program that generates a number from 1 to 10
# inclusive at random and prompts the user to "Guess a number between 1 and 10. "
# While the user's guess remains incorrect, if the guess is too small,
# prompt the user to "Guess higher! ", and otherwise prompt the user to
# "Guess lower! " When the user guesses the correct number, print "You guessed it!"


# import random
#
# rand_number = random.randint(1, 10)
# guess = int(input("Guess a number: "))
#
# while guess != rand_number:
#     if guess < rand_number:
#         print("Higher!")
#     else:
#         print("Lower!")
#
#     guess = int(input("Guess a number: "))
#
# print("You got it")



# Define a dictionary in the context of a data structure in computer science.

stuff = {
    "stuff": "things",
    True: 5,
    False: True,
    7: "bananas"
}

# Create a dictionary in Python using appropriate syntax. For example,
# you could create a dictionary of animals in a zoo, where the keys are the
# names of the animals, and the values are their ages.

monkey = {
    "name": "monkey",
    "age": 5,
    "color": "grey"
}


# Access a value in your dictionary (such as the age of one of the animals),
# both by indexing into the dictionary using the key, and by calling the ge
# method on the dictionary.

print(monkey["age"])

# Add another key-value pair into your dictionary using indexing.

monkey["height"] = "3'2"

# Modify a value in your dictionary (such as increase
# an age by 1 after an animal's birthday) using indexing.

monkey["age"] = monkey["age"] + 1

# Delete a key-value pair from your dictionary using the del keyword.

print(monkey)
del monkey["height"]
print(monkey)

# Get all the keys in your dictionary by calling the keys method on your dictionary.

print(monkey.keys())

# Get all the values in your dictionary by calling the values method on your dictionary.

print(monkey.values())


# Get all the items in your dictionary by calling the items method on your dictionary.

print(monkey.items())

# Loop through your dictionary by looping through the key-value entries.

for k, v in monkey.items():
    print(f"{k}: {v}")

# Loop through your dictionary by looping through the keys.

for k in monkey.keys():
    print(k)

# Loop through your dictionary by looping through the values.

for v in monkey.values():
    print(v)

# Create a dictionary in Python, nesting lists inside the dictionary.
# For example, you could create a dictionary of animals in a zoo, where
# the keys are the names of the animals, and the values are lists that
# contain their corresponding species, sex, and age.

monkey = {
    "name": "Bart",
    "info": ["monkey", "m", 6]
}


# As time allows, nest dictionaries inside a list.


zoo = [
    {"species": "monkey", "name": "Bart"},
    {"species": "giraffe", "name": "Chelsea"},
    {"species": "tiger", "name": "Bri"}
]

# As time allows, nest dictionaries inside a dictionary.

zoo = {
    "owner": {"name": "Barry McNulty", "age": 46},
    "animals": [
        {"species": "monkey", "name": "Bart"},
        {"species": "giraffe", "name": "Chelsea"},
        {"species": "tiger", "name": "Bri"}
    ]
}
