import random
cash = 50.0
cashmin = 50.0
mult = 0.05
last = "white"
buffer = ['white','white','white']
print(buffer)


for x in range (0 , 100):
    n = random.randint(1 , 15)
    if(n < 8):
        buffer[2] = buffer[1]
        buffer[1] = buffer[0]
        buffer[0] = "Red"

    elif(n > 7 and n != 15):
        buffer[2] = buffer[1]
        buffer[1] = buffer[0]
        buffer[0] = "Black"

    else:
        buffer[2] = buffer[1]
        buffer[1] = buffer[0]
        buffer[0] = "white"
        
    print("dice: ",n)
    print(buffer)

    if(buffer[0] == "Red" and buffer[1] == "Red" and buffer[2] == "Red" ):
            cash = cash - mult
            mult = mult*2
            last = "Red"

    elif(buffer[0] == "Black" and buffer[1] == "Black" and buffer[2] == "Black" ):
            cash = cash - mult
            mult = mult*2
            last = "Black"
            
    elif( last != "white"):
            cash = cash - mult
            mult = mult*2

    if(cash < 1):
        print("QUEBROU")
        print("cash: %.2f " % cash)
        break;
    if( cash < cashmin):
        cashmin = cash

    if(last == "Red" and buffer[0] == "Black" or last == "Black" and buffer[0]=="Red"):
        cash = cash + mult 
        mult = 0.05
        last = "white"
        
    print("cash: %.2f " % cash)

print("cashmin: %.2f " % cashmin)
