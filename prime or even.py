A=int(input("Enter number: "))
for i in range (2, A//2+1):
      if (A%i==0):
          print("Not prime")
          break
else:
    print("Prime Number")
