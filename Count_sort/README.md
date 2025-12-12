# Counting Sort Algorithm

## Overview

Counting Sort is a sorting algorithm that sorts a collection of **non-negative integers** by counting the occurrences of each unique value. Instead of comparing elements (like in Bubble or Quick Sort), Counting Sort uses an auxiliary array (called a **count array**) to keep track of how many times each value occurs. The algorithm then reconstructs the sorted array based on these counts.

### Key Features

- **Stable sorting algorithm**: maintains the relative order of equal elements.  
- **Time Complexity**: O(n + k), where n is the number of elements and k is the maximum value in the array.  
- **Space Complexity**: O(k) for the count array.  
- Works best when the range of values (k) is not significantly larger than the number of elements (n).

---

## How Counting Sort Works

### 1. Find the Maximum Value
Determine the largest number in the array to define the size of the counting array.

### 2. Create a Counting Array
- Initialize an array of zeros of size `max_val + 1`.  
- Each index represents a possible value in the original array.

### 3. Count Occurrences
- Iterate through the input array.  
- Increment the counter at the index corresponding to each value.

### 4. Rebuild the Sorted Array
- Clear the original array.  
- Loop through the counting array.  
- For each number, append it to the original array as many times as it occurred.

---

## How the Provided Code Works

```python
def counter(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    arr[:] = []
    
    for num, freq in enumerate(count):
        arr.extend([num] * freq)
    
    return arr

unsorted = list(map(int, input("Enter the values that you would want to sort using count sort separated by a comma: ").strip().split(",")))
arr_sorted = counter(unsorted)
print(f"\t----Sorted Array----\n\t{arr_sorted}")
