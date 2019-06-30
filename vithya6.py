year = int(input("Please Enter the Year Number you wish: "))

if(year%4 == 0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("%d is a Leap Year" %year)
        else:
            print("%d is Not the Leap Year" %year)
    else:
        print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
