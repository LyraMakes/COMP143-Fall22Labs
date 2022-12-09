
with open("content.txt", "r") as fin:
    content = fin.readlines()




total = 0
numLines = 0

for line in content:
    total += float(line)
    numLines += 1

average = total / numLines

with open("output.txt", "w") as fout:
    fout.write(f"{average}")


# The Collatz conjecture says that if you start from an integer greater than or equal to 1,
#
# then divide by 2 if the number is even,
#
# or triple the number and add 1 if the number is odd,
#
#
#
# then the sequence will end up at 1.


def collatz(num):
    print(num)
    if (num % 2 == 0):
        collatz(num / 2)
    elif (num > 1):
        collatz((3 * num) + 1)



print(collatz(int(input("NUM >>> "))))


def extreme(num):
    print(num)
    extreme(num + 1)

extreme(1)

