n = int(input())
first_list = []
second_list = []

for _ in range(n):
    first_list.append(int(input()))

for _ in range(n):
    second_list.append(int(input()))

if first_list == second_list:
    print("equal")
else:
    print("not equal")
