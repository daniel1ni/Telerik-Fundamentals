from collections import defaultdict

n = int(input())
foods_list = []
vowels = ['a','o','u','e','i']
#min_vowels = 20
count = 0
count_consonant = 0
word_values = {}

for i in range(n):
    food_input = input()
    foods_list.append(food_input)

word_values = dict.fromkeys(foods_list, None)

for item in foods_list:
    for char in item:
        if char in vowels:
            count += 1
    word_values[item] = count
    count = 0

print(word_values)

