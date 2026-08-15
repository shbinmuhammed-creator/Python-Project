print("1.Area of Triangle")
print("2.Peri of square")
print("3.Peri of triangle")
print("circumference of circle")
ch=int(input("enter your choice: "))
if ch==1:
        L=int(input("Enter length"))
        B=int(input("Enter Breadth"))
        Area= L*B*0.5
        print("Area of Triangle",Area)
elif (ch==2):
    L=int(input("Enter Length of one side"))
    Peri=4*L
    print("Peri of suqare",Peri)
elif ch==3:
    L=int(input("Enter Length"))
    A=3*L
    print("Peri of triangle", A)
elif ch==4:
     r=int(input("Enter radius"))
     c=2*3.14*r
     print("circumference=",c)
else:
    print("invalid choice")
    
