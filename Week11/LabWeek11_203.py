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
    total = 1.50 + pounds * (10.50 + 0.86)
    return round(total, 2)


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
    rand_num = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number 1-10: "))
        if guess == rand_num:
            print("You guessed it")
            break
        elif guess > rand_num:
            print("Lower!")
        else:
            print("Higher!")


# guessing_game()

# MinMax-ing
# Write a function to calculate the maximum
# and minimum of a passed in list
# Use a for loop to iterate through it.
# DO NOT USE "max", "min", or "sorted"


def print_max_min(nums):
    current_min = nums[0]
    for num in nums:
        if current_min > num:
            current_min = num
    print(f"Minimum: {current_min}")

    current_max = nums[0]
    for num in nums:
        if current_max < num:
            current_max = num
    print(f"Maximum: {current_max}")


# print_max_min([2, 6, 423, -100, 1, 2, 3, 423])


def get_max_min():
    current_min = 99999999999
    current_max = -99999999999

    while True:
        num = input("Enter a number (q to quit): ")
        if num == "q":
            break
        num = int(num)

        if num < current_min:
            current_min = num

        if num > current_max:
            current_max = num

    print(f"Minimum: {current_min}")
    print(f"Maximum: {current_max}")





