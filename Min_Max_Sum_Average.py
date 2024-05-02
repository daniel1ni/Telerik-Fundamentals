n = int(input())
number_list = []

for i in range(n):
    user_input = float(input())
    number_list.append(user_input)

min_value = min(number_list)
max_value = max(number_list)
sum_value = sum(number_list)
avg_value = sum(number_list) / n

print(f"min={format(min_value,".2f")}")
print(f"max={format(max_value,".2f")}")
print(f"sum={format(sum_value,".2f")}")
print(f"avg={format(avg_value,".2f")}")
