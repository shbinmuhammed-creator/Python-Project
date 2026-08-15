def listchange(arr):
     for i in range (len(arr)):
          if arr[i]%2==0:
               arr[i]=10
          else:
               arr[i]=arr[i]*5
     print(arr)
