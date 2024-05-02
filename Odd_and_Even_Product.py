list = []

n = int(input())
product_odd = 1
product_even = 1
index = 0

for i in range(0,n):
    numbers_input = int(input())
    list.append(numbers_input)

for index, value in enumerate(list):
    if index % 2 == 0:
        product_odd *= value
    else:
        product_even *= value

if product_even == product_odd:
    print(f"yes {product_even}")
else:
    print(f"no {product_odd} {product_even}")