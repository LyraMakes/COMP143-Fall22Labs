our_dict = {}
should_continue = True
while should_continue:
    key = input("Word >")
    value = input("Meaning >")
    our_dict[key] = value
    word = input()
    if (word == "c"):
        should_continue = True
    else:
        should_continue = False

print(our_dict)
