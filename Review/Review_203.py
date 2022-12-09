
dictionary = {}

while True:
    user_key = input("Enter a key: (leave blank to quit) ").strip()
    if (user_key == ""):
        break

    user_value = input("Enter a value: ").strip()
    dictionary[user_key] = user_value


print(dictionary)
#
# print("   this   ".strip() == "this")


for key, value in dictionary.items():
    print(f"Dict at {key} = {value}")






