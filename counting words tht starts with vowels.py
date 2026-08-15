a=input("Enter string:")
b=a.split()
c=0
for i in b:
     if i[0] in "aeiou" or i[0] in "AEIOU":
          c=c+1
print(c)
