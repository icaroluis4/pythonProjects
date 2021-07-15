import random
maxn = 100
dic = {}
cont = 0
bnk = 40
bnm = bnk
mult = 1
y=0

for x  in range (0 , 1700 ):
		dic[x]= 1
	
for x in range (0 , 1700):
    cont = cont + 1;
    n = random.randint(0, 99);
    print (n);
    if n < 7:
        dic[x] = 0
    if n > 53:
        dic[x] = 2
    #if cont == 10:
        #cont = 0
            
for x in range ( 0, 1700):
    #if bnk >=60.0:
            if dic[x] == 2:
                bnk = bnk + mult * (bnk * 0.025);
                mult = 1;
            else:
                bnk = bnk - mult * (bnk * 0.025);
                mult = mult * 2
            if bnk < bnm:
                bnm = bnk;
                y = x
            
    #else:
            #if dic [x] == 0:
                #bnk = bnk - 1.50;
            #else:
                #bnk = bnk+0.30;
	    
            print(" num: ", x , "--" , dic[x], "--", bnk," $")


print (" \n menor:", bnm , " rodada: " , y)
