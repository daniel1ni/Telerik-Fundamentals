number = int(input())

for x in range(1, number + 1):
    for y in range(x, x+number):
        print(y, end=' ')
    print()    
