numbers_input = input()
start_index = int(input())

list_numbers = [int(x) for x in numbers_input.split(",")]

final_list = []

start_index = start_index % len(list_numbers)

for item in list_numbers[start_index:]:
    final_list.append(item)

for item in list_numbers[:start_index]:
    final_list.append(item)


for index, item in enumerate(final_list):
    if index < len(final_list) - 1:
        print(item, end=",")
    else:
        print(item, end="")