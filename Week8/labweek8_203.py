numbers = [92, 12, 100, 0, 17, 18]

new_list = []
for i in range(len(numbers)):
    new_list.append(numbers[-1*(i+1)])
print(new_list)



# EXAMPLE --Not Real Values--:
#  i | -1*(i+1) | numbers[-1*(i+1)] | new_list
# ---+----------+-------------------+-------------------------
#  7 | -8       |       23          | [3, 4, 1]
#  8 | -9       |       42          | [3, 4, 1, 23]

