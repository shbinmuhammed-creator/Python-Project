t=()
n=int(input("Total no of students: ")
      for i in range(n):
      name=input("enter name: ")
      mark=int(input("Enter mark: ")
      avg=int(input("Enter average: ")
      t1+(name,mark,avg)
      t=t+(t1,)

ch="y"
while ch=="Y" or ch=="y":
    print("1.Result:")
    print("2.display")
    print("3.search")
    print(4."merit list")
    c=int(input("Enter your choice: "))
          if c==1:
              for i in (t):
                  if i[2]>32:
                      print(i[0],"pass")
                    else:
                        print("fail")
            elif c==2:
                print("name\t mark\t avg")
                for i in t:
                    print(i[0],i[1],i[2])
                elif c==3:
                    nm=input("Enter name to be searched")
                    for i in t:
                        if i[0]==nm:
                            print(i[0],i[1],i[2])
                        else:
                            print("not found")
            elif c==4:
                for i in t:
                    if i[2]>74:
                        print(i[0])
            else:
                print("invalid choice")
            ch=input("do you want to continue Y/N?)
                
