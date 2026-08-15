print("1.Append")
print("2.Insert element")
print("3.Extend")
print("4.Modify")
print("5.Delete element with index vlaue")
print("6.Delete element with value")
ch=int(input("Enter choice: "))
l=[1,2,3,4,5,6]
if(ch==1):
     ele=input("Element: ")
     l.append(ele)
     print(l)
elif ch==2:
     ele=int(input("Enter ele: "))
     ind=int(input("Enter index: "))
     l.insert(ind,ele)
     print(l)
elif ch==3:
     a=int(input("Enter no. of values: "))
     l1=[]
     for i in range (a):
            b=int(input("Enter values: "))
            l.append(b)
     l.extend(l1)
     print(l)
elif ch==4:
     ind=int(input("Enter element to modify: "))
     ele=int(input("New Element: "))
     l[ind]=ele
     print(l)
elif ch==5:
     ind=int(input("Enter index value: "))
     l.pop(ind)
     print(l)
elif ch==6:
     ele=int(input("Enter element to remove: "))
     l.remove(ele)
     print(l)
      
      
