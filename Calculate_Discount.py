n = int (input())
nums = []
discount = 1 - 0.65

for i in range(n):
    number = float(input())
    nums.append(number)

for x in nums:
    print(f"{(x * discount):.2f}")
