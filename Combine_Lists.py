input_one = input()
input_two = input()

list_one = [int(x) for x in input_one.split(",")]
list_two = [int(x) for x in input_two.split(",")]
combined_list = []

for i in range(len(list_one)):
    combined_list.append(str(list_one[i]))
    combined_list.append(str(list_two[i]))

print(",".join(combined_list))

