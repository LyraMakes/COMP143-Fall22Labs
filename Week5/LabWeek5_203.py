import random
names = ["Tyler Barros", "Adam Beatrice", "Jake Gonzalez", "Madelyne Guidaboni", "Aydin Hinton",
         "Dominic Indermitte", "Rodrigo Leal", "Ryan McKenzie", "Kathleen McMahon",
         "Shreya Patel", "Roshini Rajkumar", "Qichao Zhang"]

#          first      second      last
print(f"{names[0]}, {names[1]}, {names[-1]}")

prize_names = ["$1,000", "Computer", "Phone", "Gumball"]
prize_values = [  1_000,      2_000,     500,        10]

rand_prize = random.randrange(0, len(prize_names))
print(f"You won a {prize_names[rand_prize]} worth ${prize_values[rand_prize]}")

rand_prize = random.randrange(0, len(prize_names))
print(f"You won two {prize_names[rand_prize]}s worth ${prize_values[rand_prize] * 2}")

prize_values[3] = 10_010

rand_prize = random.randrange(0, len(prize_names))
print(f"You won two {prize_names[rand_prize]}s worth ${prize_values[rand_prize] * 2}")


print(f"Minimum Prize value: {min(prize_values)}")
print(f"Maximum Prize value: {max(prize_values)}")
print(f"Total Prize value: {sum(prize_values)}")

