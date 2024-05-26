# Print "yes" if the array is in Wave Form - e.g. first > second < third > fourth < fifth >
# Print "no" if the array is not in Wave Form

usr_inp = input().split()
numbers = [int(i) for i in usr_inp]


res = 'yes'
for i in range(1, len(numbers)-1):
    if (numbers[i] >= numbers[i-1]) and (numbers[i] <= numbers[i+1]):
        res = 'no'
    
    elif (numbers[i] <= numbers[i-1]) and (numbers[i] >= numbers[i+1]):
        res = 'no'
    

print(res)