n = int(input())

for _ in range(n):

    numbers_input = input()

    num_list = [int(x) for x in numbers_input.split(" ")]

    counter = 0


    for i in range(len(num_list)):
        
        if num_list[i] == num_list[len(num_list)-1-i]:
            counter += 1
    if counter == len(num_list):
            print("Yes")
    else:
            print("No")

    #print(', '.join(map(str, num_list)))