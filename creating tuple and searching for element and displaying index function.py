t=()
n=int(input("Enter no. of elements: "))
for i in range(n):
     ele=int(input("Enter element: "))
     t=t+(ele)
print(t)
a=int(input("Enter element to be searched: "))
for i in (t):
             if i==a:
                  print(t.index(a))
             else:
                  print("Error")
