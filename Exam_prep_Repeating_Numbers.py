n = int(input())

num_list = []

for i in range(n):
    user_input = int(input())
    num_list.append(user_input)

counts = {}

for element in num_list:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1

most_common_element = max(counts, key=counts.get)

print(most_common_element)