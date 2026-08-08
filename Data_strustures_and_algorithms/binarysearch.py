mylist=list(range(0,100_000_000))
Target=90_000_000
low=0
high=50_000_000-1
while (True):
    middle=int((low+high)/2)
    if mylist[middle]==Target:

        print("Found the the number at position",middle)
        break
    elif mylist[middle]<Target:
        low=middle+1
    elif mylist[middle]>Target:
        high=middle-1