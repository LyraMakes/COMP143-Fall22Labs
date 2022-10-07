import random

names = ["Joseph Davis", "Danny Isaza",
         "Cail Lee", "Patrick Lee", "Cam Magee"]
print(f"{names[0]}, {names[1]}, {names[-1]}")

print(names[random.randrange(0, len(names))])
print(random.choice(names))


prize_names = ["Goldfish",  "Car", "Stuffed Animal", "Movie Tickets"]
prize_values = [        2, 60_000,          100_000,             20]

rand_prize = random.randrange(0, len(prize_names))
rand_name = random.randrange(0, len(names))
print(f"{names[rand_name]} won a {prize_names[rand_prize]} worth ${prize_values[rand_prize]}")


prize_values[2] = 200_000

for i in range(4):
    rand_prize = random.randrange(0, len(prize_names))
    rand_name = random.randrange(0, len(names))
    print(f"{names.pop(rand_name)} won a {prize_names.pop(rand_prize)} worth ${prize_values.pop(rand_prize)}")

