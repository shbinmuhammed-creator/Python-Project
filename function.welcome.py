def l(a):
     c=0
     b=a.split()
     for i in range (1,len(b)-1):
          if 'l' in b[i]:
               c=c+1
     print("No. of l=",c)
a=input("Enter string")
l(a)
