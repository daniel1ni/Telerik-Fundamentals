n = int(input())
output = []

for i in range(1, n+1):
    if i % 7 != 0 and i % 3 != 0:
        output.append(i)
print(*output)