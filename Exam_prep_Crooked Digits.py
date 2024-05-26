number = input()
number_to_list = []

for item in number:
    if item.isdigit():
        number_to_list.append(item)

sum = 0

for digit in number_to_list:
    sum += int(digit)

while sum > 9:
    temp = int()
    for digit in str(sum):
        temp += int(digit)
    sum = temp

print(sum)
    
    