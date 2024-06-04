user_input = input()
converted_input = user_input.split(",")

budget = int(converted_input[0])
price = int(converted_input[1])
exchange_ratio = int(converted_input[2])

beers_purchased = budget // price
beers_drinked = beers_purchased
empties = beers_purchased

while empties >= exchange_ratio:
    beers_drinked += empties // exchange_ratio
    empties -= empties // exchange_ratio
  
#5//2=2
#5%2=1
print(beers_drinked)
