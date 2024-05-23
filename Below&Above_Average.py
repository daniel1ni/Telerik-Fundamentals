numbers_input = input()

main_list = [int(x) for x in numbers_input.split(",")]

avg = sum(main_list) / len(main_list)
below = []
above = []

for item in main_list:
    if item < avg:
        below.append(item)
    elif item > avg:
        above.append(item)

if avg == 0:
    print("avg: 0.00")
else:
    print("avg: " + ("%.2f" % avg))
print("below: " + ','.join(map(str, below)))
print("above: " + ','.join(map(str, above)))