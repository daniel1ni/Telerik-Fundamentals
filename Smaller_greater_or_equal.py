n = int(input())
number_list = []

for i in range(n):
    user_input = int(input())
    number_list.append(user_input)

sign_list = []

for i in range(len(number_list)-1):
    if number_list[i] < number_list[i+1]:
        sign_list.append('<')
    elif number_list[i] > number_list[i+1]:
        sign_list.append('>')
    elif number_list[i] == number_list[i+1]:
        sign_list.append('=')

combined_list = []

while True:
    try:
        combined_list.append(number_list.pop(0))
        combined_list.append(sign_list.pop(0))
    except IndexError:
        break

print(*combined_list,sep='')
