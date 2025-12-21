# Binary Search Algorithm

## What is Binary Search?

Binary Search is an efficient algorithm used to find the position of a target value within a **sorted** array (list). It works by repeatedly dividing the search interval in half:

1. Start with the entire array.
2. Find the middle element.
3. If the middle element equals the target, return its index.
4. If the target is less than the middle element, continue searching the left half.
5. If the target is greater than the middle element, continue searching the right half.
6. Repeat steps 2-5 until the target is found or the search interval is empty.

Binary Search runs in **O(log n)** time complexity, which is much faster than a linear search on large datasets.

---

## How This Code Works

```python
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
