num_list = []
prime_list = []

n = int(input())

for i in range(1, n+1):
    numbers_input = int(i)
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
for i in range(len(num_list) -1, -1, -1):
    if num_list[i] in prime_list:
        index_last_prime = i
        break

for i in range(len(prime_list)):
    end_value = prime_list[i]
    for num in num_list:
        if num <= end_value:
            if num in prime_list:
                print(1, end="")
            else:
                print(0, end="")
    print()
