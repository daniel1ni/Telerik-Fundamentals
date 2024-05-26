#185
#1+8+5 #14
#1*8*5 #40
#1+8*5 #41
#1*8+5 #13

number = input()
digit_list = [int(digit) for digit in number]
max_number = 1
results = []


temp = digit_list[0] + digit_list[1] + digit_list[2]
results.append(temp)
temp = digit_list[0] * digit_list[1] * digit_list[2]
results.append(temp)
temp = digit_list[0] + digit_list[1] * digit_list[2]
results.append(temp)
temp = digit_list[0] * digit_list[1] + digit_list[2]
results.append(temp)

print(max(results))

