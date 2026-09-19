Mylist=[47, 392, 118, 275, 64, 431, 209, 356, 17, 483,
142, 298, 75, 411, 236, 89, 327, 154, 468, 51,
213, 374, 102, 289, 445, 33, 196, 351, 127, 492]
for number in range(9):

    for number in range(9-1):
        if Mylist[number]<Mylist[number+1]:
            Mylist[number],Mylist[number+1]=Mylist[number+1],Mylist[number]
print(Mylist)