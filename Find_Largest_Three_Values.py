list = []

n = int(input())

for i in range(0,n):
    numbers_input = int(input())
    list.append(numbers_input)

list.sort(reverse=True)

max_value_1 = list[0]
max_value_2 = list[1]
max_value_3 = list[2]

print(f"{max_value_1}, {max_value_2} and {max_value_3}")
