input_celsius = input()

list_celsius = [int(x) for x in input_celsius.split(" ")]

t_Fahrenheit = 0

for item_celsius in list_celsius:
    t_Fahrenheit = item_celsius * (9/5) + 32
    print(round(t_Fahrenheit))
