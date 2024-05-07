user_input = ""
longest_food = ""

while user_input != "END":
    user_input = input()
    if user_input != "END" and len(user_input) >= len(longest_food):
        longest_food = user_input

print(longest_food)