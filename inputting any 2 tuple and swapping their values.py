T1=()
n=int(input("Enter number of elements: "))
for i in range(n):
      ele=int(input("Enter element:"))
      T1=T1+(ele,)
T2=()
m=int(input("Enter no of element:"))
for i in range(m):
    ele1=int(input("Enter element: "))
    T2=T2+(ele1,)
T1,T2=T2,T1
print("Swapped T1= ", T2)
print("swappedT2= ", T1)
              
