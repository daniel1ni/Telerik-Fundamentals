n = int(input())
buildings_list = []

for i in range(n):
    user_input = input()
    buildings_list.append(user_input)

windows_list = []
new_buildings_list = []

for building in buildings_list:
    alone_building = building.split(" ")
    windows = int(alone_building[1]) * int(alone_building[2])
    building += " " + str(windows)
    new_buildings_list.append(building)
    windows_list.append(windows)   
    windows = 0

total_price = 0
price = 0

for item in new_buildings_list:
    new_item = item.split(" ")
    if new_item[0] == "Residential":
        price = 0.75 * int(new_item[3])
    elif new_item[0] == "Business":
        price = 1.25 * int(new_item[3])
    elif new_item[0] == "Mall":
        price = 2.00 * int(new_item[3])
    print(f"{price:.2f}$")
    total_price += price

print(f"Total: {total_price:.2f}$")
    
    








    








