n = int(input())
x = float(input())
factorial = 1
sum_divided_by_x = 0

for i in range(1, n + 1):
    factorial = factorial * i
    sum_divided_by_x += factorial / (x ** i)

s = 1 + sum_divided_by_x

print("%.5f" %s)
