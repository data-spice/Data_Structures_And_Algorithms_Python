def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    #Splitting arr
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    
    #recursive split
    righthalf=mergesort(righthalf)
    lefthalf=mergesort(lefthalf)
    
    return merge(lefthalf,righthalf)

def merge(left,right):
    results=[]
    i=j=0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            results.append(left[i])
            i+=1
        else:
            results.append(right[j])
            j+=1
    
    results.extend(left[i:])
    results.extend(right[j:])
    
    return results

unsorted=list(map(int,input("Enter the elements you want to sort separated by a comma: ").strip().split(",")))
sorted= mergesort(unsorted)
print(sorted)