numbers_input = input()

num_list = [int(x) for x in numbers_input.split(", ")]

num_list.sort()
num_list.reverse()

print(', '.join(map(str, num_list)))