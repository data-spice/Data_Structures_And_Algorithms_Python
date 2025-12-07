# Bubble Sort Algorithm

## Overview

Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. This process repeats until the list is sorted.

Although it is easy to understand and implement, Bubble Sort is inefficient for large datasets because of its **O(n²)** time complexity.

---

## How Bubble Sort Works

1. Compare each pair of adjacent elements in the list.
2. Swap them if they are in the wrong order (e.g., if the first element is greater than the second for ascending sort).
3. Repeat these steps for each element in the list, reducing the range after each pass as the largest elements "bubble" to the end.
4. Stop when no swaps are needed on a new pass, indicating the list is sorted.

---

## Example

Consider the list: `[5, 3, 8, 4, 2]`

- First pass: Compare and swap as needed  
  `[3, 5, 4, 2, 8]`  
- Second pass:  
  `[3, 4, 2, 5, 8]`  
- Third pass:  
  `[3, 2, 4, 5, 8]`  
- Fourth pass:  
  `[2, 3, 4, 5, 8]` (Sorted!)

---

## Python Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break
    return arr

# Example usage
numbers = [5, 3, 8, 4, 2]
sorted_numbers = bubble_sort(numbers)
print("Sorted list:", sorted_numbers)
