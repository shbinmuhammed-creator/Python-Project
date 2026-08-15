A=int(input("Enter values"))
L=[]
for i in range(A):
    B=int(input("Enter elements"))
    L.append(B)
    for i in L:
        if L.count(i)>1:
            L.remove(i)
print(L)
