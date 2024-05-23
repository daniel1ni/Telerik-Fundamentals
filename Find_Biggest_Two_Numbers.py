numbers_input = input()

num_list = [int(x) for x in numbers_input.split(" ")]

biggest_nums = []

num_list.sort()
num_list.reverse()
num_list = num_list[:2]

print(' '.join(map(str, num_list)))