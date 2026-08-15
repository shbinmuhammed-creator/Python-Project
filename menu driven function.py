def rectarea(a,b):
     area=a*b
     print("area of rect: ",area)
     return area
def rectperi (a,b):
     peri=2*(a+b)
     print("Perimeter of rectangle:", peri)
     return peri
def circarea(a):
     area=3.14*a*a
     print("Circle area: ",area)
     return area
def circperi(a):
     peri=2*3.14*a
     print("peri:",peri)
     return peri
ch="y"
while ch=="y":
     print("1.area of rectangle")
     print("2.perimeter of rectangle:")
     print("3.Area of circle:")
     print("4.Peri of circle:")
     c=int(input("Enter choice:"))
     if c==1:
          a=int(input("Enter length: "))
          b=int(input("Enter breadth: "))
          print(rectarea(a,b))
     elif c==2:
          a=int(input("Enter length:"))
          b=int(input("Enter Breadth:"))
          print(rectperi(a,b))
     elif c==3:
          r=int("Enter radius")
          print(circarea(a))
     elif c==4:
          r=int(input("Enter radius"))
          print(circperi(r))
     
     
