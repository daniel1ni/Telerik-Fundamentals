elements_input = input()

main_list = [int(x) for x in elements_input.split(",")]

negatives = [x for x in main_list if x < 0]
zeroes = [x for x in main_list if x == 0]
positives = [x for x in main_list if x > 0]

result = negatives + zeroes + positives

print(','.join(map(str, result)))