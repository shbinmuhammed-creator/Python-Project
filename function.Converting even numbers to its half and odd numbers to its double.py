def pythonconvert(L):
     for i in range(len(L)):
          if L[i]%2==0:
               L[i]=L[i]//2
          else:
               L[i]=L[i]*2
     print(L)
L=[2,3,4]
pythonconvert(L)
