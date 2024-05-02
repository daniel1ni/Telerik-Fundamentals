card_sign = input()
card_color = ["clubs","diamonds","hearts","spades"]
card_suite = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
index = card_suite.index(card_sign)

for x in card_suite[0:index+1]:
    print(f"{x} of spades, {x} of clubs, {x} of hearts, {x} of diamonds")
 