number = int(input())

temp = input()
counter = number - 1

while counter:
    current_input = input()
    counter -=1
    if temp.replace("-", "").isnumeric() and current_input.replace("-", "").isnumeric():
        temp = str(int(temp) + int(current_input))
    
    elif temp.replace("-", "").isnumeric() and current_input.replace("-", "").isalpha():
        print(temp)
        temp = current_input

    elif temp.replace("-", "").isalpha() and current_input.replace("-", "").isalpha():
        temp += "-" + current_input
    
    elif temp.replace("-", "").isalpha() and current_input.replace("-", "").isnumeric():
        print(temp)
        temp = current_input
    
    elif not current_input.isalnum():
        print(temp)
        print(current_input)
        temp = input()
        counter -= 1

print(temp)
    