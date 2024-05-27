usr_inp = input().split(', ')
target = int(input())
num_array = [int(i) for i in usr_inp]
temp_list = []

for i in range(1, len(num_array)-1):
    item = num_array[i]
    previous_item = num_array[i - 1]
    next_item = num_array[i + 1]
    if item == target and previous_item != target and next_item != target:
        if previous_item > next_item:
            temp_list.append(previous_item)
        elif previous_item < next_item:
            temp_list.append(next_item)

temp_index = 0
for i in range(1, len(num_array)-1):
    if num_array[i] == target:
        num_array[i] = temp_list[temp_index]
        temp_index = (temp_index + 1) % len(temp_list)

print(num_array)
        