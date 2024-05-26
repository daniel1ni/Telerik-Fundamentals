n = int(input())

numbers_input = input()

num_list = [int(x) for x in numbers_input.split(" ")]

pairs = []

x = False

#да зачистя pairs след всяко пълнене

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] + num_list[j] == n:
            pairs.append((num_list[i], num_list[j]))
            for pair in pairs:
                print(f"{pair[0]},{pair[1]}")
                x = True
            pairs.clear()

if x is False:
    print("no pairs")

#print(', '.join(map(str, num_list)))