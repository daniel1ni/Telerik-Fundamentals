basicBill = 12.00

textMessagesQuantity = int(input())
minutesQuantity = int(input())

messagesOver = textMessagesQuantity - 20
if messagesOver < 0:
    messagesOver = 0
minutesOver = minutesQuantity - 60
if minutesOver < 0:
    minutesOver = 0

messagesOverAmount = messagesOver * 0.06
minutesOverAmount = minutesOver * 0.1

tax = (messagesOverAmount + minutesOverAmount) * 0.2

totalBill = tax + basicBill + messagesOverAmount + minutesOverAmount


print(f"{messagesOver} additional messages for {format(messagesOverAmount,".2f")} levas")
print(f"{minutesOver} additional minutes for {format(minutesOverAmount,".2f")} levas")
print (f"{format(tax,".2f")} additional taxes")
print(f"{format(totalBill,".2f")} total bill")