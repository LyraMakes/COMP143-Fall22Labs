
# User input
# Write a Python program that prompts the user with
# "How many pounds of coffee do you want to order? "
# and calculates the cost of the order to be shipped from 1369 Coffee House.
# The shop charges $1.50 in overhead costs per order and sells the coffee for $10.50
# a pound plus the cost of shipping. Each order ships for $0.86 per pound.
# State the total cost to the customer using appropriate formatting,
# including rounding the price to two decimal digits (up to the penny).

pounds = int(input("How many pounds of coffee do you want to order? "))
total = 1.50 + (10.50 + 0.86) * pounds
print(f"Your total comes to ${total}")
print(f"This would get you {pounds * 30} cups of coffee")



# While
# Write a Python program that generates a number from 1 to 10
# inclusive at random and prompts the user to "Guess a number between 1 and 10. "
# While the user's guess remains incorrect, if the guess is too small,
# prompt the user to "Guess higher! ", and otherwise prompt the user to
# "Guess lower! " When the user guesses the correct number, print "You guessed it!"
import random, webbrowser

rand_number = random.randint(1, 10)
guess = -1

while guess != rand_number:

    guess = int(input("Guess a number: "))

    if guess < rand_number:
        print("Higher!")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")
    elif guess > rand_number:
        print("Lower!")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")

print("You got it")





