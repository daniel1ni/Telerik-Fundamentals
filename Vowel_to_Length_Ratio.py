n = int(input())
vowels = str("aouei")
best_word = ""
max_vowels = 0
ratio = 1

for _ in range(n):
    food = input()
    vowels_counter = 0
    for i in food:
        if i in vowels:
            vowels_counter += 1
    if vowels_counter / len(food) < ratio:
        best_word = food
        max_vowels = vowels_counter
        ratio = vowels_counter / len(food)
    elif vowels_counter / len(food) == ratio and vowels_counter == max_vowels and len(best_word) < len(food):
        best_word = food
        max_vowels = vowels_counter
        ratio = vowels_counter / len(food)
    elif vowels_counter / len(food) == ratio and vowels_counter > max_vowels:
        best_word = food
        max_vowels = vowels_counter
        ratio = vowels_counter / len(food)

print(f"{best_word} {max_vowels}/{len(best_word)}")
