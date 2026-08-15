m=int(input("Enter your salary"))
if m<50000:
    print("tax= ",m*0.07)
elif m>=60000 and m<80000:
    print("tax=",m*0.08)
elif m>=80000 and m<100000:
    print("tax=", m*0.08)
else:
    print("tax=",m*0.10)
