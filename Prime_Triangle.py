num_list = []
prime_list = []

n = int(input())

for i in range(n):
    numbers_input = int(input())
    num_list.append(numbers_input)

def is_prime(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

for num in num_list:
    if is_prime(num):
        prime_list.append(num)

index_last_prime = 0
for item in num_list:
    if item in prime_list:
        index_last_prime = num_list.index(item)


for i in range(len(prime_list)):
    for j in range(i+1):
        print(num_list[j], end=" ")
    print()
