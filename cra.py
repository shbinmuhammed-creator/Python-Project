x=0
z=1
for i in range(1,3):
    for j in range(1,i):
        Z=i+j-1
        if(Z%2==0):
            x=x+Z
        elif(Z%3==0):
            x=x+Z-2
    print("x=",x)
            
