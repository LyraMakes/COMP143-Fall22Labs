# Write a function that reads a column of numbers from a file,
# calculates the average, and writes the average to a file.


def process():
    with open("content.txt", "r") as infile:
        content = infile.readlines()

    num = len(content)

    total = 0
    for line in content:
        total += float(line.strip())

    average = total / num

    with open("output.txt", "w") as outfile:
        outfile.write(f"{average}")


process()


# Use recursion to generate a Collatz sequence from a user-specified positive number.

# The Collatz conjecture says that if you start from an integer greater than or equal to 1,
# then divide by 2 if the number is even,
# or triple the number and add 1 if the number is odd,
# then the sequence will end up at 1.


def collatz(num):
    print(num)

    if num % 2 == 0:
        collatz(num / 2)
    elif num > 1:
        collatz((3 * num) + 1)


# collatz(5)



# (a) Without using a computer, predict the output of this code, given user input values of your choice.
# (b) What is the purpose of the function?
# (c) This code does not work if the initial input is "q".
#     Correct the code so that it handles this case correctly.
# (d) Check all of your work by running code.

def main():
    total = 0
    count = 0
    x = input("Enter a number (q for quit) ")
    while (x != "q"):
        total = total + float(x)
        count += 1
        x = input("Enter a number (q for quit) ")
    if count != 0:
        print("Result: ", total / count)


main()
