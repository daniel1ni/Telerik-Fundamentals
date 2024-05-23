elements_input = input()

main_list = [x for x in elements_input.split(",")]

result = []
[result.append(x) for x in main_list if x not in result]

result = ','.join(result)

print(result)


