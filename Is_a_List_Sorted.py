n = int(input())

for _ in range(n):

    numbers_input = input()

    num_list = [int(x) for x in numbers_input.split(",")]

    counter = 1


    for i in range(len(num_list) - 1):
        
        if num_list[i] <= num_list[i+1]:
            counter += 1
    if counter == len(num_list):
            print("true")
    else:
            print("false")

    #print(', '.join(map(str, num_list)))