month_1 = "Dragon"
month_2 = "Snake"
month_3 = "Horse"
month_4 = "Sheep"
month_5 = "Monkey"
month_6 = "Rooster"
month_7 = "Dog"
month_8 = "Pig"
month_9 = "Rat"
month_10 = "Ox"
month_11 = "Tiger"
month_12 = "Hare"

year = int(input())

if year == 2000: print(month_1)
if year == 2001: print(month_2)
if year == 2002: print(month_3)
if year == 2003: print(month_4)
if year == 2004: print(month_5)
if year == 2005: print(month_6)
if year == 2006: print(month_7)
if year == 2007: print(month_8)
if year == 2008: print(month_9)
if year == 2009: print(month_10)
if year == 2010: print(month_11)
if year == 2011: print(month_12)

if year > 2011:
    if (year - 2000) % 12 == 0: print(month_1)
    if (year - 2001) % 12 == 0: print(month_2)
    if (year - 2002) % 12 == 0: print(month_3)
    if (year - 2003) % 12 == 0: print(month_4)
    if (year - 2004) % 12 == 0: print(month_5)
    if (year - 2005) % 12 == 0: print(month_6)
    if (year - 2006) % 12 == 0: print(month_7)
    if (year - 2007) % 12 == 0: print(month_8)
    if (year - 2008) % 12 == 0: print(month_9)
    if (year - 2009) % 12 == 0: print(month_10)
    if (year - 2010) % 12 == 0: print(month_11)
    if (year - 2011) % 12 == 0: print(month_12)

if year < 2000:
    if -(year - 2000) % 12 == 0: print(month_1)
    if -(year - 2001) % 12 == 0: print(month_2)
    if -(year - 2002) % 12 == 0: print(month_3)
    if -(year - 2003) % 12 == 0: print(month_4)
    if -(year - 2004) % 12 == 0: print(month_5)
    if -(year - 2005) % 12 == 0: print(month_6)
    if -(year - 2006) % 12 == 0: print(month_7)
    if -(year - 2007) % 12 == 0: print(month_8)
    if -(year - 2008) % 12 == 0: print(month_9)
    if -(year - 2009) % 12 == 0: print(month_10)
    if -(year - 2010) % 12 == 0: print(month_11)
    if -(year - 2011) % 12 == 0: print(month_12)
