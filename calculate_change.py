price = float(input())
paid = float(input())
change = round(((paid - price) * 100),2)

if change // 100 != 0:
    print((int(change//100)),"x 1 lev")
    change -= (change // 100) * 100
if change // 50 != 0:
    print((int(change//50)),"x 50 stotinki")
    change -= (change // 50) * 50
if change // 20 != 0:
    print((int(change//20)),"x 20 stotinki")
    change -= (change // 20) * 20
if change // 10 != 0:
     print((int(change//10)),"x 10 stotinki")
     change -= (change // 10) * 10
if change // 5 != 0:
    print((int(change//5)),"x 5 stotinki")
    change -= (change // 5) * 5
if change // 2 != 0:
     print((int(change//2)),"x 2 stotinki")
     change -= (change // 2) * 2
if change == 1:
    print((int(change//1)),"x 1 stotinka")