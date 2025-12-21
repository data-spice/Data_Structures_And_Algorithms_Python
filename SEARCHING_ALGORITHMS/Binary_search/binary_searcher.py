def bin_srch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

arr = list(map(int, filter(None, input("Enter values separated by a comma: ").strip().split(","))))
arr.sort()  

target = int(input("Enter the number you would like to search for: ").strip())

index = bin_srch(arr, target)

if index != -1:
    print("Value", target, "found at index", index)
else:
    print("Target not found in array.")
