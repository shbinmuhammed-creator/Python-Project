N=input("Enter name: ")
P=input("Enter Pass; ")
if N=="admin" or P=="root":
    print("You are admin")
elif N=="User" or P=="root":
    print("You are guest")
elif N=="guest":
    print("you are guest")
else:
    print("Not Valid")
    
       
