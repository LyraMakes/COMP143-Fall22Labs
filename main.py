import random

prizes = {
    "Goldfish": 2,
    "Car": 60_000,
    "Stuffed Animal": 100_000,
    "Movie Tickets": 20
}

key, value = random.choice(prizes)

print(f"Won a {key} worth {value}")