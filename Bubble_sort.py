import random
Mylist=[]
for number in range(4000):
    Mylist.append(random.randint(0,1000))

for number in range(len(Mylist)):

    for number in range(len(Mylist)-1):
        if Mylist[number]<Mylist[number+1]:
            Mylist[number],Mylist[number+1]=Mylist[number+1],Mylist[number]
print(Mylist)