def counter (arr):
    if not arr:
        return arr
    max_val=max(arr)
    count=[0]*(max_val +1)
    
    for num in arr:
        count[num]+=1
    
    arr[:]=[]
    
    for num,freq in enumerate(count):
        arr.extend([num]*freq)
    return arr

unsorted=list(map(int,input("Enter the values that you would want to sort using count sort separated by a comma: ").strip().split(",")))
arr_sorted=counter(unsorted)
print(f"\t----Sorted Array----\n\t{arr_sorted}")