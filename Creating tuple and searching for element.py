T=()
f=0
n=int(input("Enter no of elements: "))
for i in range(n):
    ele=int(input("Enter element"))
    T=T+(ele,)
print(T)
A=int(input("Enter element to search: "))
for i in (T):
    if i==A:
        print(T.index(A))
        f=1
if f==0:
        print("Error")
        
