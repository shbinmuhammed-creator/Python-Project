d={}
s=input("Enter string: ")
for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)
for key in d:
    print(key,":",d[key])
