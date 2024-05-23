numbers_input = input()

positive = []
negative = []
combined_list = []

list_numbers = [int(x) for x in numbers_input.split(" ")]

for digit in list_numbers:
    if digit < 0:
        negative.append(digit)
    else:
        positive.append(digit)


combined_list = negative + positive

for i in combined_list:
    print(i, end=" ")