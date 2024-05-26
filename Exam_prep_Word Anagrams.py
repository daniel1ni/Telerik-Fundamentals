anagram = input()
n = int(input())

anagram_sorted = ''.join(sorted(anagram))

for i in range(n):
    user_input = input()
    user_input_sorted = ''.join(sorted(user_input))
    if anagram_sorted == user_input_sorted:
        print("Yes")
    else:
        print("No")
    
