def ballanced(number):
    number_to_list = []
    for item in str(number):
        number_to_list.append(int(item))
    if number_to_list[0] + number_to_list[2] == number_to_list[1]:
        return True

total_ballanced = 0

while True:
    number_input = input()
    ballanced(number_input)
    if ballanced(number_input):
        total_ballanced += int(number_input)

    if not ballanced(number_input):
        break

print(total_ballanced)
    
    