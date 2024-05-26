usr_inp = input().split(',')
numbers = [int(i) for i in usr_inp]

zero_list = []

for item in numbers:
    if item == 0:
        zero_list.append(item)

while 0 in numbers:
    numbers.remove(0)

numbers = numbers + zero_list

print(",".join(map(str, numbers)))

