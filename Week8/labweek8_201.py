# import random
#
# numbers = []
# for i in range(6):
#     numbers.append(random.randint(1, 1_000_000))
#
# print(numbers)







numbers = [92, 12, 100, 0, 17, 18]




new_list = []
for i in range(len(numbers)):
    new_list.append(numbers[-1*(i+1)])
print(new_list)

# numbers = [92, 12, 100, 0, 17, 18]
#  i | -1*(i+1) | numbers[-1*(i+1)] | new_list
# ---+----------+-------------------+-------------------------
#  0 | -1       |  18               | [18]
#  1 | -2       |  17               | [18, 17]
#  2 | -3       |   0               | [18, 17, 0]
#  3 | -4       | 100               | [18, 17, 0, 100]
#  4 | -5       |  12               | [18, 17, 0, 100, 12]
#  5 | -6       |  92               | [18, 17, 0, 100, 12, 92]

# numbers =  [92, 12, 100, 0, 17, 18]
# new_list = [18, 17, 0, 100, 12, 92]






# === Separate Topic ===

# numbers = [92, 12, 100, 0, 17, 18]

# Find the maximum of this list
# Use the concept of iterating through a loop to do so
# Don't use the -1*(i+1) construct though, that was just to reverse the loop
# Don't use the builtin max() either


