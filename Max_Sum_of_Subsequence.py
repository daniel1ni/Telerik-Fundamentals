n = int(input())
numbers = []

for _ in range(n):
    usr_inp = input()
    numbers.append(int(usr_inp))

max_sum = 1
temp = 0

for num in numbers:
    temp += num
    if temp >= max_sum:
        max_sum = temp
    if temp < 0:
        temp = 0

print(max_sum)

#print(",".join(map(str, numbers)))

