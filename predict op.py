L1="neat"
x=""
L1=[]
count=1
for i in L1:
    if i in ['a','e','i','o','u',]:
        x=x+i.swapcase()
    else:
            if(count%2)!=0:
                x=x+str((len(L1[:count])))
            else:
                x=x+i
            count=count+1
print(x)
