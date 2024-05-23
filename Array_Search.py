elements_input = input()
missing_digits = []

main_list = [int(x) for x in elements_input.split(",")]

for i in range(1, len(main_list)+1):
    if i not in main_list:
        missing_digits.append(i)

print(','.join(map(str, missing_digits)))