list = []

n = int(input())
max_value = -200

for i in range(0,n):
    numbers_input = int(input())
    list.append(numbers_input)

for value in list:
    if value > max_value:
        max_value = value
print(max_value)