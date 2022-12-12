with open("example.txt", "w") as outfile:
    outfile.write("Line 1\nLine 2")



with open("example.txt", "r") as infile:
    content = infile.readlines()
    print(content)
    for line in content:
        print(line.strip())


def main():
    total = 0
    count = 0
    x = input("Enter a number (q for quit) ")
    while (x != "q"):
        total = total + float(x)
        count += 1
        x = input("Enter a number (q for quit) ")
    try:
        print("Result: ", total / count)
    except ZeroDivisionError:
        print("Enter at least one number!")

# main()
try:
    with open("extempt.txt", "r") as f:
        print(f.readlines())

except FileNotFoundError:
    print("COunrt ")



