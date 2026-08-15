s=int(input("Enter salary: "))
if s<=60000:
      print("tax=",60000*0.07)
elif s>60000 and s<80000:
     print("Tax= ",s*0.08)
elif s>80000 and s<100000:
     print("tax= ",s*0.09)
else:
     print("tax= ",s*0.10)
      
