from collections import Counter
n = int(input())
numbers = []

for _ in range(n):
    usr_inp = input()
    numbers.append(int(usr_inp))

counter = Counter(numbers)

max_count = max(counter.values())

most_common_elements = [k for k, v in counter.items() if v  == max_count]

smallest_most_common = min(most_common_elements)

print(smallest_most_common)

#print(",".join(map(str, numbers)))

