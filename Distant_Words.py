input_number = input()
 
target_number = int(input_number)

number_of_words = int(input())


sum_of_all_characters = 0

for i in range(number_of_words):

    letter = input()

    letter = letter.lower()

    current_word_score = 0

    for char in letter:
        current_word_score += ord(char) - ord('a') + 1

    print(f"{letter} {abs(target_number-current_word_score)}")

    sum_of_all_characters += abs(target_number-current_word_score)


print("{:.2f}".format(sum_of_all_characters/number_of_words))
 