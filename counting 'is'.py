A=input("Enter sentence: ")
c=0
A.split()
for i in A:
    if i=="is" or i=="IS":
        c=c+1
print("Number of time 'is' appears=",c)
