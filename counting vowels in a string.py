word=input("Enter word:")
c=0
for i in word:
    if i in "aeiou" or i in "AEIOU":
        c=c+1
print("Number of vowels=",c)
