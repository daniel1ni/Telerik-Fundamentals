n = int(input())
numbers_list = []

for i in range(0,n):
    number = int(input())
    numbers_list.append(number)

max_length = 1
current_length = 1
current_number = numbers_list[0]

for i in range(1, len(numbers_list)):
    if numbers_list[i] == current_number:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_number = numbers_list[i]
        current_length = 1

if current_length > max_length:
    max_length = current_length

print(max_length)