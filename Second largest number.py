a=int(input("Enter total ele:"))
L=[]
for i in range (a):
    B=int(input("Enter element"))
    L.append(B)
print(L)
L.sort()
print(L[-2])
