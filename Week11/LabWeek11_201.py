import random

# User input
# Write a python function that given a number of pounds of coffee,
# it would calculate the total cost.
# There is a $1.50 overhead cost,
# coffee sells for $10.50 per pound,
# and shipping is $0.86 per pound.
# Pass the value to the function using "input()",
# and print the result rounding to the nearest penny.


def get_coffee_total(pounds):
    return round(1.50 + (10.50 + 0.86) * pounds, 2)


# total_pounds = float(input("How many pounds of coffee would you like? "))
# total_cost = get_coffee_total(total_pounds)
# print(f"Your total is {total_cost}")

# While

# Write a python function that starts, and handles a guessing game
# Generate a random number from 1-10 inclusively once, then
# Loop and prompt the user to guess.
# If the guess is too low, or too high,
# print out "Higher!" or "Lower!", respectively.
# If the guess is correct, break out of the loop and
# print "You guessed it!"


def guessing_game():
    rand_int = random.randint(1, 10)
    while True:
        guess = int(input("Enter a guess [1-10]: "))

        if guess == rand_int:
            break
        elif guess > rand_int:
            print("Lower!")
        else:
            print("Higher!")

    print("You got it!")


# guessing_game()

# MinMax-ing
# Write a function to calculate the maximum
# and minimum of a passed in list
# Use a for loop to iterate through it.
# DO NOT USE "max", "min", or "sorted"


def print_max_min(nums):
    cur_min = 999999999999
    cur_max = -999999999999

    for num in nums:
        if num < cur_min:
            cur_min = num
        if num > cur_max:
            cur_max = num

    print(f"Maximum: {cur_max}")
    print(f"Minimum: {cur_min}")


# print_max_min([1, 2, 17, -8, 12.2, 3, 0, 4])


def get_max_min():
    cur_min = 999999999999
    cur_max = -999999999999

    while True:
        num = input("Enter a integer (q to quit): ")

        if num == "q":
            break
        num = int(num)

        if num < cur_min:
            cur_min = num
        if num > cur_max:
            cur_max = num

    print(f"Maximum: {cur_max}")
    print(f"Minimum: {cur_min}")


get_max_min()
