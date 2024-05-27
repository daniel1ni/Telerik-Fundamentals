num = str(input())
evens = []
odds = []

for char in num:
    digit = int(char)
    if digit % 2 == 0:
        evens.append(digit)
    else:
        odds.append(digit)

sum_evens = sum(evens)
sum_odds = sum(odds)

if sum_evens > sum_odds:
    print(f"{sum_evens} energy drinks")
elif sum_odds > sum_evens:
    print(f"{sum_odds} cups of coffee")
else:
    print(f"{sum_evens} of both")   


