
# Dictionaries:

gabagool = {"color": "red", "points": 5}

print(gabagool["color"])
print(gabagool["points"])

its_color = gabagool.get("color")
its_points = gabagool.get("points")

print(its_color)
print(its_points)

gabagool["position"] = "(23, 4)"


gabagool2 = {}
gabagool2["stuff"] = "others"


gabagool3 = {'color': 'red', 'points': 5}
print(gabagool3)
gabagool3['color'] = 'pink'
gabagool3['points'] = 10
print(gabagool3)





gabagool4 = {'color': 'red', 'points': 5}
print(gabagool4)
del gabagool4['points']
print(gabagool4)


# Store people's favorite languages.
fav_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }


# Show each person's favorite language.
for name, language in fav_languages.items():
    print(f"{name}: {language}")

# Show everyone who's taken the survey.
for name in fav_languages.keys():
    print(name)

# Show all the languages that have been chosen.
for language in fav_languages.values():
    print(language)


num_responses = len(fav_languages)



# Start with an empty list.
users = []
# Make a new user, and add them to the list.
new_user = {
    'last': 'fermi',
    'first': 'enrico',
    'username': 'efermi',
}

users.append(new_user)
# Make another new user, and add them as well.
new_user = {
    'last': 'curie',
    'first': 'marie',
    'username': 'mcurie',
}
users.append(new_user)
# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(f"{k}: {v}")
        print("\n")



# Define a list of users, where each user
# is represented by a dictionary.
users = [
    {
        'last': 'fermi',
        'first': 'enrico',
        'username': 'efermi',
    },
    {
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie',
    },
]
# Show all information about each user.
for user_dict in users:
    for k, v in user_dict.items():
        print(f"{k}: {v}")
        print("\n")

# Store multiple languages for each person.
fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Show all responses for each person.
for name, langs in fav_languages.items():
    print(f"{name}: ")
    for lang in langs:
        print(f"- {lang}")



users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
 }


for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


squares = {}
for x in range(5):
    squares[x] = x**2

squares = {x: x**2 for x in range(5)}


group_1 = ['kai', 'abe', 'ada', 'gus', 'zoe']
group_2 = ['jen', 'eva', 'dan', 'isa', 'meg']
pairings = {name: name_2 for name, name_2 in zip(group_1, group_2)}



aliens = []
# Make a million green aliens, worth 5 points
# each. Have them all start in one row.
for alien_num in range(1000000):
    new_alien = {}
    new_alien['color'] = 'green'
    new_alien['points'] = 5
    new_alien['x'] = 20 * alien_num
    new_alien['y'] = 0
    aliens.append(new_alien)
# Prove the list contains a million aliens.
num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)
