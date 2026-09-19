def Merge_sort(Mylist):
    if len(Mylist)<=1:
    
      
      return(Mylist) 
    
    print(Mylist)
    Middle=len(Mylist)//2
    print(Middle)
    Left=Mylist[0:Middle]
    print(Left)
    Right=Mylist[Middle:]
    print(Right)

    Left=Merge_sort(Left)
    Right=Merge_sort(Right)
    return Compare(Left,Right)
def Compare(Left,Right):
    Sorted_list=[]
    i=0
    j=0
    while i<len(Left)and j<len(Right):

        if Left[i]<Right[j]:
            Sorted_list.append(Left[i])
            i+=1
        elif Right[j]<Left[i]:
            Sorted_list.append(Right[j])
            j+=1
    Sorted_list.extend(Left[i:])
    Sorted_list.extend(Right[j:])
    return(Sorted_list)
Ans=Merge_sort([47, 392, 118, 275, 64, 431, 209, 356, 17, 483,
142, 298, 75, 411, 236, 89, 327, 154, 468, 51,
213, 374, 102, 289, 445, 33, 196, 351, 127, 492])
print(Ans)
