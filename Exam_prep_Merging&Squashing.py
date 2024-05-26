n = int(input())
numbers = []
pairs = []
merged = []
squashed = []

for _ in range(n):
    usr_inp = input()
    numbers.append(int(usr_inp))

for i in range(len(numbers)-1):
    combined_str = str(numbers[i]) + str(numbers[i+1])
    pairs.append(combined_str)

result = []
for s in pairs:
    digits = [int(char) for char in s]
    result.append(digits)


for group in result:
    temp = ""
    temp += str(group[1])
    temp += str(group[2])
    merged.append(temp)
    temp = ""

for group in result:
    temp = ""
    temp += str(group[0])
    sum = group[1] + group[2]
    sum %= 10
    temp += str(sum)
    temp += str(group[3])
    squashed.append(temp)
    temp = ""

print(" ".join(map(str, merged)))
print(" ".join(map(str, squashed)))

