import random


# Problem 1
def favorite_book(title):
    """prints out the formatted title"""
    print(f"One of my favorite books is {title.title()}.")


favorite_book("the lightning thief")
favorite_book("hidden figures")


# Problem 2
def fiftyPercentIncrease(number):
    """prints out the value 1.5 times more than the number"""
    print(f"Fifty percent more than {number} is {number * 1.5}!")


fiftyPercentIncrease(100)
fiftyPercentIncrease(2)


# Problem 3
def make_shirt(size, message):
    """prints out summary of shirt with size and message"""
    print(f"Created shirt of size '{size}' with message '{message}'")


make_shirt("M", "Walk a mile in my shoes. You'll end up at the library.")


# Problem 4
def countdown():
    """Prints a countdown from 10-1 then 'Zero'"""
    for i in range(10, 0, -1):
        print(i)
    print("Zero!")


countdown()


#Problem 5
def countToMax():
    """Counts up to the specified number"""
    num = int(input("How high would you like to count? "))
    for i in range(0, num + 1):
        print(i)


countToMax()
countToMax()


def roots(a, b, c):
    """Determine whether the roots are real, complex, or repeated"""
    result = (b ** 2) - (4 * a * c)
    if result > 0:
        print("There are two real roots.")
    elif result < 0:
        print("The roots are complex.")
    else:
        print("There is a repeated root.")


# Problem 7
def repackageData(salaries):
    """Separates values greater than 1,000,000 and lesser than 1,000,000"""
    greater = []
    lesser = []

    for val in salaries:
        if val > 1_000_000:
            greater.append(val)
        else:
            lesser.append(val)

    print("Greater then 1 Mil:")
    for val in greater:
        print(val)

    print("Lesser then 1 Mil:")
    for val in lesser:
        print(val)


def conversation():
    """Simulates a short conversation"""
    items = ["sword", "teddy bear", "pink bath cap"]
    number = random.randrange(len(items))

    print(f"I can't find my {items[number]}")

    sentence = random.randrange(3)

    if sentence == 0:
        print(f"I had the royal guards watch over your {items[number]} for you.")
    elif sentence == 1:
        print(f"Your {items[number]} is just as cute as can be.")
    else:
        print(f"I'm finished using your {items[number]} now.")


conversation()


# Problem 9
def square(side):
    """Returns the area of the square with the given side length"""
    return side * side # side ** 2


print(square(3))


# Problem 10
def gpa(a, b, c, d, f):
    total = a + b + c + d + f
    points = (a * 4) + (b * 3) + (c * 2) + (d * 1) + (f * 0)
    return points / total


def main():
    print(f"GPA: {gpa(3, 1, 1, 0, 0)}")
    print(f"GPA: {gpa(2, 0, 1, 2, 1)}")
    print(f"GPA: {gpa(1, 2, 1, 5, 8)}")


main()
