def bubble_sort_count(arr):
    # TODO: sort arr, and count every swap you make
    totalswaps=0
    for number in range(len(arr)):
        for number in range(len(arr)-1):
            if arr[number][1]<arr[number+1][1]:
                totalswaps+=1
                arr[number],arr[number+1]=arr[number+1],arr[number]
    return arr,totalswaps  


print(bubble_sort_count([("Amy", 72), ("Ben", 95), ("Cleo", 60), ("Dan", 88)]))
# Expected: ([1, 2, 4, 5, 8], some number of swaps)


def merge(left, right):
    i=0
    j=0 
    sorted_list=[] 
    while i<3 and j<3:
        print(i,j)
          
        if left[i]<right[j]:
            sorted_list.append(left [i])
            i+=1
        
        elif right[j]<left[i]:

            sorted_list.append(right [j])
            j+=1
    return sorted_list 
      
print(merge([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
  