x = int(input())
y = int(input())
target = int(input())
sum = 0

for number in range(x, y+1):
    for digit in str(number):
        sum += int(digit)
    if sum == target:
        print(number)
    sum = 0
