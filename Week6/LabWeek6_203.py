#!/usr/bin/env python3

def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    # problem6()
    # problem8()
    # problem10()
    pass


# Problem 1
def problem1():
    x = 4
    for i in range(3):
        print(x)
# Output
# 4
# 4
# 4


def problem2():
    x = 6
    for i in range(2):
        print(i)

# Output
# 0
# 1


# Problem 3
def problem3():
    x = 6
    for i in range(1, x):
        print('pickles')
# Output
# pickles
# pickles
# pickles
# pickles
# pickles


# Problem 4
def problem4():
    for j in range(1, 3):
        print('Greetings')
        print('\t and salutations')
# Output
# Greetings
#      and salutations
# Greetings
#      and salutations


# Problem 5
# What is your understanding of the code `for i in range(10):`?
# What does a for loop do?
# What is the role of the indentation?
# Can it be omitted?


# Problem 6
def problem6():
    print("x, y\n----")
    for x in range(4):
        print(f"{x}, {2 * x + 1}")
# Output
# 0, 1
# 1, 3
# 2, 5
# 3, 7

# Problem 7
# What is the purpose of the code in (6) above?
# What are pros and cons of the output from the Python code
# in helping a person understand a mathematical function?


# Problem 8
def problem8():
    b = 1
    print("x, y\n----")
    for x in range(4):
        print(f"{x}, {-x ** 2 / 2 + (b + 1 / 2) * x}")
# Output
# 0,
#
#
#


# Problem 9
# What is the purpose of the code in (8) above?


# Problem 10
def problem10():
    number = 5355
    digits = []
    # [Determine and state the purpose of the for loop here after some analysis.]
    for i in range(4):
        digits.append(number // 10 ** i % 10)
    digits.sort()
    small = digits[0] * 10 ** 3 + digits[1] * 10 ** 2 + digits[2] * 10 + digits[3]
    large = digits[3] * 10 ** 3 + digits[2] * 10 ** 2 + digits[1] * 10 + digits[0]
    print(f"{large=}")
    print(f"{small=}")

    number = large - small
    print(number)


if __name__ == "__main__":
    main()
