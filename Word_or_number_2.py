number = int(input())
total_sum = 0
words = ""

for i in range(number):
    input_from_user = input()
    if input_from_user.isdigit():
        input_from_user = int(input_from_user)
        total_sum += input_from_user
    else:
        words += input_from_user + "-"

if words == "":
    print("no words")

else:
    print(f"{words[:-1]}")
    
print(total_sum)
