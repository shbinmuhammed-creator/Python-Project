
a=int(input("Enter number: "))
for i in range (2,a//2+1):
     if a%i ==0:
          print(" not Prime number!")
          break
else:
               print("PRIME!")
