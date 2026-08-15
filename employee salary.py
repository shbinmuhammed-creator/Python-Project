a=int(input("Enter no. of employee: "))
d={}
for i in range (a):
    name=input("Enter Name: ")
    salary=int(input("Enter Salary: "))
    house=input("Enter house: ")
    d[name]=[salary,house]
print(d)
